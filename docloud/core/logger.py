#coding=utf8

from __future__ import print_function, division, absolute_import

import logging
import logging.config

from docloud.settings import basic


def logger_init():
    logging.config.dictConfig(basic.LOGGING)