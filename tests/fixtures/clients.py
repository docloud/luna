# coding=utf8

import pytest
from luna.clients.http import HTTPClient


@pytest.fixture('session', autouse=True)
def http_client():
    return HTTPClient(auto_decode=True, port=8200)
