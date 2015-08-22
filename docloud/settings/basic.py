#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console', 'other'],
        'level': 'INFO'
    },
    'filters': {
        'is_mobile': {
            '()': 'docloud.core.logger.MobileFilter',
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
            'filename': '/var/log/docloud/request.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 250M
            'backupCount': 5,
        },
        'exception': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/docloud/exception.log',
            'mode': 'a',
            'maxBytes': 262144000,  # 250M
            'backupCount': 5,
        },
        'other': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'uniform',
            'filters': [],
            'filename': '/var/log/docloud/record.log',
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
            'datefmt':'%Y-%m-%d %H:%M:%S.000',
        },
    }
}