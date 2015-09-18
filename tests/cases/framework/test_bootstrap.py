# coding=utf8

from flask import Flask
from docloud.api import api_init
from docloud.server import show_routers
from docloud.clients.http import HTTPClient


def test_api_init():
    app = Flask(__name__)
    api_init(app)
    show_routers(app)


def test_bootstrap_ping(http_client):
    response = http_client.get('bootstrap/ping')
    assert response.get('status')


if __name__ == '__main__':
    test_api_init()
    import IPython
    IPython.embed()
