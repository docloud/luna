#coding=utf8

from __future__ import print_function, division, absolute_import

import logging
import logging.config

from flask import request
from docloud.settings import basic


class MobileFilter(logging.Filter):
    def filter(self, record):
        ua = request.headers.get('User-Agent', '').lower()
        check_list = [
            'android' in ua,
            'iphone' in ua,
            'ipod' in ua,
            'ipad' in ua,
        ]
        if any(check_list):
                return True
        else:
            return False


def logger_init():
    logging.config.dictConfig(basic.LOGGING)