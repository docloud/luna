# coding=utf8

import os
import requests
from luna import config, logger


class HTTPClient(requests.Session):
    def __init__(self, host, port=80, token=None, prefix=None,
                 ssl=False, **kwargs):
        super(HTTPClient, self).__init__()

        self.host = host
        self.port = port

        # Enable SSL
        span = ['https:/'] if ssl else ['http:/']

        # Construct base URL
        span.append(':'.join([host, str(port)]))
        if prefix:
            span.append(prefix)

        self.url_prefix = span
        self.url = '/'.join(self.url_prefix)
        logger.info("Client bind to {url}".format(url=self.url))

        self.last = None
        self.exception = None

    def request(self, method, url, **kwargs):
        if os.environ.get('CI'):
            return {}
        url_req = '/'.join([self.url, url])
        try:
            response = super(HTTPClient, self).request(method, url_req, **kwargs)
        except Exception as e:
            self.exception = e
            raise
        else:
            self.last = response

        try:
            return response.json()
        except:
            return response.text


http = HTTPClient(config['app']['host'], config['app']['port'])
