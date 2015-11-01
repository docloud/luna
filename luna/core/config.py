# coding=utf8

"""
Copyright 2015 Luna Project

A module to handle default config settings.
"""

import os
from .exc import LunaException
from toolkit.config import parse_file


class Config(object):
    __DEFAULTS__ = {}

    @property
    def defualts(self):
        return self.__DEFAULTS__


class APPConfig(Config):
    __DEFAULTS__ = {
        'HOST': 'localhost',
        'PORT': 8021,
        'DEBUG': False
    }


class DeployConfig(Config):
    __DEFAULTS__ = {
        'USER': None,
        'PASS': None,
        'HOST': [],
    }


class MysqlConfig(Config):
    __DEFAULTS__ = {
        'HOST': 'localhost',
        'PORT': 3306,
    }


class MongoDBConfig(Config):
    __DEFAULTS__ = {
        'HOST': 'localhost',
        'PORT': 27017,
    }


class RedisConfig(Config):
    __DEFAULTS__ = {
        'HOST': 'localhost',
        'PORT': 6379,
    }


class LoggingConfig(Config):
    __DEFAULTS__ = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'handlers': ['console', 'request', 'exception'],
            'level': 'INFO'
        },
        'filters': {
            'is_mobile': {
                '()': 'luna.core.logger.MobileFilter',
            },
        },
        'loggers': {},
        'handlers': {
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
        },
        'formatters': {
            'uniform': {
                'format': '%(asctime)s %(levelname)s %(name)s [%(process)d]: '
                          '%(module)s => %(funcName)s => '
                          '%(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S.000',
            },
        }
    }


def choice(checker, seq):
    """
    Choice item from a sequence that pass the checker.

    :param seq: a sequence the checker excepted.
    :param checker: checker function, return True or False
    :return: the first item that checker function return True

    Usage:

        choice(lambda x: x % 3 == 0, [1, 2, 3, 4])
        >>> 3
    """
    if not callable(checker):
        raise LunaException('checker must be callable.')
    for item in seq:
        if item is None:
            continue
        print(item)
        if checker(item):
            return item
    return None


def load_config(path=None):
    """
    Load config file from current directory. now support environment files.

    :param path:
    :return:
    """
    path = choice(os.path.exists, [
        path,
        'env.yaml',
        'env.yml',
        'env.json',
        'env.py'
    ])
    if not path:
        config_dict = {}
    else:
        config_dict = parse_file(path)
    Config = type('Config', (object,), config_dict)
    return Config()


config = load_config()