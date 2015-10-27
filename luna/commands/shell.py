# coding=utf8

import IPython
from luna.clients.http import HTTPClient


def shell():
    http = HTTPClient(auto_decode=True, port=8200)
    IPython.embed()
