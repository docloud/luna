#coding=utf8

from __future__ import print_function, division, absolute_import

from flask import Flask
from docloud.core.logger import logger_init
from docloud.core.auth import auth_init

def init(settings):
    app = Flask(__name__)

    app.config.update(**settings.APP)

    logger_init()

    auth_init(app)
