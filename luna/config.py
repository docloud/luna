# coding=utf8

"""
Copyright 2015 Luna Project

A module to handle default config settings.
"""

import six
import yaml
import logging
import logging.config
from .exceptions import LunaException


class ConfigError(LunaException):
    pass


class DefaultConfig(object):
    __DEFAULTS__ = {
        "id": None,
        "name": "default",
        "app": {
            'host': '127.0.0.1',
            'port': 3000,
            'debug': False
        },
        "deploy": {
            'host': '127.0.0.1',
            'port': 3000
        },
        "redis": {
            'host': '127.0.0.1',
            'port': 6379
        },
        "mongodb": {
            'host': '127.0.0.1',
            'port': 27017
        },
        "mysql": {
            'host': '127.0.0.1',
            'port': 3306
        },
        "logging": {
            'version': 1,
            'disable_existing_loggers': False,
            'root': {
                'handlers': ['console', 'request', 'exception'],
                'level': 'INFO'
            },
            'filters': {},
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
    }

    @staticmethod
    def valid(config):
        pass

    @classmethod
    def set_default(cls, config):
        for k, v in six.iteritems(cls.__DEFAULTS__):
            config.setdefault(k ,v)
        cls.valid(config)
        return config

    @classmethod
    def load(cls, path="app.yaml"):
        try:
            config = yaml.load(open("app.yaml"))
        except IOError:
            config = cls.set_default({})
            logging.config.dictConfig(config["logging"])
            logger = logging.getLogger(__name__)
            logger.info("Could not load environment config, use default.")
        else:
            config = cls.set_default(config)
            logging.config.dictConfig(config["logging"])
        return config
