# coding=utf8

from flask import Flask
from docloud.api import api_init
from docloud.server import show_routers


def test_api_init():
    app = Flask(__name__)
    api_init(app)
    show_routers(app)


def test_bootstrap_ping(http_client):
    response = http_client.get('bootstrap/ping')
    assert response.get('status')


def test_bootstrap_not_found(http_client):
    response = http_client.get('bootstrap/ping/')
    assert http_client.ret.status_code == 404


def test_bootstrap_exception_01(http_client):
    response = http_client.get('bootstrap/ping_x')
    assert response.get('code') == 800


def test_bootstrap_exception_02(http_client):
    response = http_client.get('bootstrap/ping_x', json={'name': 'demo'})
    assert response.get('name') == 'demo'


if __name__ == '__main__':
    import IPython
    IPython.embed()
