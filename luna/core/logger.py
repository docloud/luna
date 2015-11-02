# coding=utf8

"""
Copyright 2015
"""

import logging
import logging.config

from flask import request
from luna.core.config import config


class MobileFilter(logging.Filter):
    def filter(self, record):
        ua = request.headers.get('User-Agent', '').lower()
        term = ('android', 'iphone', 'ipod', 'ipad')
        if any([t in ua for t in term]):
            return True
        else:
            return False


def logger_init(app):
    logging.config.dictConfig(config.logging)


def get_logger():
    if not request:
        return logging.getLogger(config.name)
    else:
        return logging.getLogger(config.name)


logger = get_logger()
