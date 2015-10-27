# coding=utf8

from __future__ import print_function, division, absolute_import

import logging
import logging.config

from flask import request
from luna.settings import basic


class MobileFilter(logging.Filter):
    def filter(self, record):
        ua = request.headers.get('User-Agent', '').lower()
        term = ('android', 'iphone', 'ipod', 'ipad')
        if any([t in ua for t in term]):
            return True
        else:
            return False


def logger_init():
    logging.config.dictConfig(basic.LOGGING)