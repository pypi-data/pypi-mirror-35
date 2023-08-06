import pytest


import os
import asyncio
import threading

from toolkit import free_port
from apistellar import Application
from uvicorn.main import Server, HttpToolsProtocol
from .parser import Parser


def run_server(app, port=8080):
    """
    创建一个简单的server用来测试
    :param app:
    :param port:
    :return:
    """
    loop = asyncio.new_event_loop()
    protocol_class = HttpToolsProtocol

    server = Server(app, "127.0.0.1", port, loop, None, protocol_class)
    loop.run_until_complete(server.create_server())
    if server.server is not None:
        loop.create_task(server.tick())
        loop.run_forever()


@pytest.fixture(scope="module")
def create_server():
    def run(app):
        port = free_port()
        th = threading.Thread(target=run_server, args=(app, ), kwargs={"port": port})
        th.setDaemon(True)
        th.start()
        return port
    return run


@pytest.fixture(scope="module")
def normal_server_port(create_server, request):
    old_path = os.getcwd()
    try:
        path = os.path.dirname(request.module.__file__)
        app = Application("test", current_dir=path)
        yield create_server(app)
    finally:
        os.chdir(old_path)


@pytest.fixture(scope="session")
def parser():
       return Parser("mock.json")


@pytest.fixture(scope="module")
def mock(request, parser: Parser, monkeypatch):
    mocks = getattr(request.module, "MOCKS")
    if mocks:
        for mock in parser.find_mock(*mocks):
            monkeypatch.setattr(*mock)

