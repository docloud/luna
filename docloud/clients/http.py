#!/usr/bin/env python
# coding=utf8

from __future__ import print_function, division, absolute_import

import requests


class HTTPClient(requests.Session):
    """
    HTTP 请求类

    :param prefix: 请求URL的前缀
    :param cookies: 自动附加的Cookie
    :param headers: 自动附加的Header
    :return: HTTP请求返回值，字典或字符串
    """
    def __init__(self, host='127.0.0.1', port=3000, token=None, auto_decode=False, **kwargs):
        super(HTTPClient, self).__init__()

        self.host = host
        self.port = port
        self.token = token

        self.ret = None
        self.exception = None
        self.auto_decode = auto_decode

    def request(self, method, url, **kwargs):
        if self.port:
            request_url = 'http://{}:{}/api/{}'.format(self.host, self.port, url)
        else:
            request_url = 'http://{}/api/{}'.format(self.host, url)

        try:
            response = super(HTTPClient, self).request(method, request_url, **kwargs)
        except Exception as e:
            self.exception = e
            raise
        else:
            self.ret = response

        if 'auto_decode' in kwargs:
            auto_decode = kwargs.get('auto_decode')
        else:
            auto_decode = self.auto_decode

        if not auto_decode:
            return self.ret

        try:
            return self.ret.json()
        except:
            return self.ret.text

    def refresh_token(self, token=None):
        if token:
            self.token = token

        self.headers.update({'Authorization': self.token})