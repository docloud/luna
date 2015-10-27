#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

APP = {
    'HOST': '127.0.0.1',
    'PORT': 8200,
    'DEBUG': False,
    'LOGGER_NAME': 'Docloud',
    'SECRET_KEY': '\x96\xdb\xd4s\xd1\xa6\xd5R\x1bq{p\xf5\xfa_y\xeda\xdc\x11sP\xba\xd6',
}

MONGODB = {
    'conn': 'mongodb://localhost:27017/',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console', 'other'],
        'level': 'INFO'
    },
    'filters': {
        'is_mobile': {
            '()': 'luna.core.logger.MobileFilter',
        },
    },
    'loggers': {
        'request': {
            'handlers': ['request'],
            'propagate': True,
            'level': 'INFO'
        },
        'exception': {
            'handlers': ['exception'],
            'propagate': True,
            'level': 'WARN'
        },
    },
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
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/luna/exception.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 250M
            'backupCount': 5,
        },
        'other': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/luna/record.log',
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
