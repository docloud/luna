# coding=utf8

APP = {
    'HOST': '127.0.0.1',
    'PORT': 8200,
    'DEBUG': False,
    'LOGGER_NAME': '{{ project }}',
    'SECRET_KEY': '{{ gen_salt() }}',
}

MONGODB = {
    'conn': 'mongodb://localhost:27017/',
}

REDIS = {
    'conn': 'redis://localhost:6379/',
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
            'datefmt': '%Y-%m-%d %H:%M:%S.000',
        },
    }
}
