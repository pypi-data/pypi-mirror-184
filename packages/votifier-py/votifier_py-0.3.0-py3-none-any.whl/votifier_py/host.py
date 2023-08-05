from __future__ import annotations
from abc import abstractmethod

import hashlib
import hmac
import json
import secrets
import struct
from base64 import b64encode
from pathlib import Path
from queue import Queue
from socket import socket as Socket
from socketserver import TCPServer, BaseRequestHandler, ThreadingMixIn
from threading import Event, Thread
import logging
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from pydantic.main import BaseModel


logger = logging.getLogger("votifier_py")


class VotifierException(Exception):
    pass


class Vote(BaseModel):
    username: str
    serviceName: str
    timestamp: int
    address: str
    challenge: str | None = None
    uuid: str | None = None


class VoteRequest(BaseModel):
    signature: str
    payload: str

    def get_payload(self):
        return Vote(**json.loads(self.payload))


class VotifierHandler(BaseRequestHandler):
    def handle(self):
        try:
            logger.info(f'{self.client_address[0]} connected.')
            self.request: Socket
            self.server: VotifierServer  # type: ignore
            self.request.settimeout(3)

            # Handshake reply
            challenge = secrets.token_hex(12)
            reply = b'VOTIFIER 2 ' + challenge.encode() + b'\n'
            self.request.sendall(reply)

            # Read preamble
            magic_bytes = self.request.recv(2)
            if len(magic_bytes) < 2:
                raise VotifierException('Received empty message.')
            (magic_number,) = struct.unpack(">H", magic_bytes)
            if magic_number == 0x733A:
                return self._nuvote(reply, challenge)
            else:
                return self._votifier1(magic_bytes)
        except VotifierException as e:
            logger.error(str(e))
        finally:
            logger.info(f' Closing connection to {self.client_address[0]}.')

    def _votifier1(self, buffer: bytes) -> None:
        buffer += self.request.recv(256)  # Yes, 2 + 256 = 258. This is to check whether the client sends too much data.
        length = len(buffer)
        if length != 256:
            raise VotifierException(f'Client sent {length} bytes instead of 256.')
        data: list[str] = PKCS1_v1_5.new(key=self.server.rsa_private_key).decrypt(buffer, sentinel=b'').decode('utf8').split('\n')

        if not (4 < len(data) <= 6):
            raise VotifierException(f'Received garbled or incorrect data: "{data}". Wrong encryption key?')

        header, service_name, username, address, timestamp, *_ = data

        if header != 'VOTE':
            raise VotifierException(f'Expected "VOTE", got "{header}". Wrong encryption key?')

        self.server._vote_queue.put(
            Vote(
                username=username,
                timestamp=int(timestamp),
                address=address,
                serviceName=service_name,
            )
        )
        logger.info(f'Vote cast by "{username}"')

    def _nuvote(self, reply: bytes, challenge: str) -> None:
        '''Read payload. Assumes magic bytes are read and correct'''
        header = self.request.recv(2)
        (length,) = struct.unpack(">H", header)
        # Read payload
        vote_request: VoteRequest = self.read_vote_request(length)
        payload: Vote = vote_request.get_payload()

        # Validate challenge-response
        if payload.challenge != challenge:
            self._reply_error()
            raise VotifierException(f'Challenge mismatch. Sent: {reply}, got back: {vote_request}')
        expected_signature = self.make_signature(vote_request.payload.encode())

        if expected_signature != vote_request.signature:
            self._reply_error()
            raise VotifierException(f'Token mismatch. Got signature "{vote_request.signature}", expected: "{expected_signature}"')

        # process vote and send response
        self.server._vote_queue.put(payload)
        logger.info(f'Vote cast by "{payload.username}"')
        self.request.sendall(b'{"status": "ok"}')

    def _reply_error(self):
        '''Reply with error message, disregard broken connections.'''
        try:
            self.request.sendall(b'{"status": "error"}')
        except Exception:
            pass

    def make_signature(self, payload: bytes):
        private_key: bytes = self.server._token  # type: ignore
        return b64encode(hmac.digest(private_key, payload, hashlib.sha256)).decode()

    def read_vote_request(self, length: int) -> VoteRequest:
        payload_bytes = self.request.recv(length)
        payload_str = payload_bytes.decode()
        data = json.loads(payload_str)
        return VoteRequest(**data)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    def __init__(self, ip: str, port: int, token: bytes) -> None:
        self.shutdown_event = Event()
        self._main_thread: Thread | None = None
        self._vote_queue: Queue[Vote] = Queue()
        self._token: bytes = token
        TCPServer.__init__(self, (ip, port), VotifierHandler)

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *_):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def server_bind(self) -> None:
        self.allow_reuse_address = True
        super().server_bind()
        logger.info(f'Votifier server listening on {self.server_address[0]}:{self.server_address[1]}')

    def shutdown(self) -> None:
        self.shutdown_event.set()
        TCPServer.shutdown(self)
        ThreadingMixIn.server_close(self)
        if self._main_thread is not None:
            del self._main_thread
            self._main_thread = None

    def start_serving(self, poll_interval: float = 0.2) -> None:
        '''Non-blocking start.'''
        if self._main_thread is not None:
            raise VotifierException('Attempting to start already running server. Aborting.')
        # Set flag
        self._poll_interval = poll_interval
        self._main_thread = Thread(target=self.serve_forever)
        self._main_thread.start()


class VotifierServer(ThreadedTCPServer):
    def __init__(self, ip: str = 'localhost', port: int = 8192, secrets_folder: str | Path = 'secrets') -> None:
        self.port: int = port
        self.ip: str = ip

        self.secrets_folder: Path = Path(secrets_folder)
        self.token_file: Path = self.secrets_folder / 'votifier2.token'
        self.rsa_private_key_file: Path = self.secrets_folder / 'rsa.private'
        self.rsa_public_key_file: Path = self.secrets_folder / 'rsa.public'

        self.secrets_folder.mkdir(exist_ok=True)

        if not self.token_file.exists():
            VotifierServer.generate_token(self.token_file)

        if not self.rsa_private_key_file.exists():
            VotifierServer.generate_rsa_keypair(self.rsa_private_key_file, self.rsa_public_key_file)

        token = self.get_private_key(self.token_file)
        self.rsa_private_key: RSA.RsaKey = self.load_rsa_private_key(self.rsa_private_key_file)
        ThreadedTCPServer.__init__(self, ip=ip, port=port, token=token)

    def get_private_key(self, path: Path) -> bytes:
        with open(path, 'rb') as f:
            return f.read().strip(b'\n ')

    def wait_for_vote(self, timeout: float | None = None) -> Vote:
        return self._vote_queue.get(block=True, timeout=timeout)

    @classmethod
    def generate_rsa_keypair(cls, private_file: Path, public_file: Path):
        key = RSA.generate(2048)
        private = key.export_key('PEM', pkcs=8)
        public = key.public_key().export_key('PEM', pkcs=8)
        with open(private_file, "wb") as pr, open(public_file, "wb") as pb:
            pr.write(private)
            pb.write(public)

    def load_rsa_private_key(self, file: Path) -> RSA.RsaKey:
        with open(file, "rb") as f:
            return RSA.import_key(f.read())

    @classmethod
    def generate_token(cls, file: str | Path):
        with open(file, 'w') as f:
            f.write(secrets.token_urlsafe(260))

    def _start(self) -> None:
        with self:
            self.serve_forever()

    def start(self) -> VotifierServer:
        self.start_serving()
        logger.info('Server started')
        return self

    def stop(self) -> None:
        '''Stop votifier server'''
        logger.info('Stopping server')
        self.shutdown()
        logger.info('Server stopped')

    def __enter__(self) -> VotifierServer:
        self.start()
        return self

    def __exit__(self, *_):
        self.stop()
