# coding=utf8

import IPython
from docloud.clients.http import HTTPClient


def shell():
    http = HTTPClient(auto_decode=True)
    IPython.embed()