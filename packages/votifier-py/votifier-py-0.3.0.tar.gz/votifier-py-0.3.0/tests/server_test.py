import pytest
from aiovotifier import VotifierClient

from votifier_py import Vote, VotifierServer


@pytest.mark.asyncio
async def test_server_rsa() -> None:
    server: VotifierServer = None  # type: ignore
    try:
        port = 9998
        server = VotifierServer(port=port, secrets_folder='secrets').start()

        with open('secrets/rsa.public', 'r') as f:
            public_key = f.read()

        client = VotifierClient('127.0.0.1', port=port, service_name='TestService', secret=public_key)

        promise = await client.vote('user', '10.0.0.1')

        vote: Vote = server.wait_for_vote()
        assert vote.username == 'user'
        assert promise is None or promise.get('status', '') == 'ok'
    finally:
        if server is not None:
            server.stop()


@pytest.mark.asyncio
async def test_server_nuvotifier() -> None:
    server: VotifierServer = None  # type: ignore
    try:
        port = 9998
        server = VotifierServer(port=port, secrets_folder='secrets').start()

        with open('secrets/votifier2.token', 'r') as f:
            token = f.read()

        client = VotifierClient('127.0.0.1', port=port, service_name='TestService', secret=token)

        promise = await client.nu_vote('user', '10.0.0.1')

        vote: Vote = server.wait_for_vote()
        assert vote.username == 'user'
        assert promise.get('status', '') == 'ok'
    finally:
        if server is not None:
            server.stop()
