# coding=utf8

import IPython
from luna import config
from luna.clients.http import HTTPClient


def shell(host=None, port=None):
    client_host = host or config.app['host']
    client_port = port or config.app['port']
    http = HTTPClient(auto_decode=True, host=client_host, port=client_port)
    IPython.embed()
