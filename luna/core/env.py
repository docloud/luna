# coding=utf8

from __future__ import absolute_import, division, print_function

import os
from .exc import LunaException
from .utils import choice
from toolkit.config import parse


def is_dev_environ():
    return not os.environ.get('deploy_machine', False) == 'develop'


def Config(dict):
    def to_dict(self):
        d = {}
        for k, v in self.__dict__.iteritems():
            if not k.startswith('__') and k.is_upper():
                d[k] = v
        return d


class APPConfig(Config):
    HOST = 'localhost'
    PORT = 8021
    DEBUG = False


class MysqlConfig(Config):
    HOST = 'localhost'
    PORT = 3306


class MongoDBConfig(Config):
    HOST = 'localhost'
    PORT = 27017


class RedisConfig(Config):
    HOST = 'localhost'
    PORT = 6379


class LoggingConfig(Config):
    VERSION = 1
    DISABLE_EXISTING_LOGGERS = False
    ROOT = {
        'handlers': ['console', 'request', 'exception'],
        'level': 'INFO'
    }
    FILTERS = {
        'is_mobile': {
            '()': 'luna.core.logger.MobileFilter',
        },
    }
    LOGGERS = {},
    HANDLERS = {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'uniform',
            'filters': [],
        },
        'request': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/luna/request.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 250M
            'backupCount': 5,
        },
        'exception': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/luna/exception.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 250M
            'backupCount': 5,
        }
    }
    FORMATTERS = {
        'uniform': {
            'format': '%(asctime)s %(levelname)s %(name)s [%(process)d]: '
                      '%(module)s => %(funcName)s => '
                      '%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S.000',
        },
    }


def load_default_config():
    return {}


def load_config(path):
    path = choice(os.path.exists, [
        path,
        'env.yaml',
        'env.yml',
        'env.json',
        'env.py'
    ])
    if not path:
        raise LunaException('Environment is not exists.')

    config = load_default_config()
    config.update(parse(path))
    return type('Config', (dict,), config)
