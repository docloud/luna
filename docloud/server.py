#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Flask
from docloud import settings
from docloud.api import api_init
from docloud.core.logger import logger_init
from docloud.core.auth import auth_init
from docloud.core.db import db_init
from docloud.core.exc import exc_init


def init(settings):
    app = Flask(__name__)

    app.config.update(**settings.basic.APP)

    api_init(app)

    logger_init()

    auth_init(app)

    db_init(settings.basic)

    exc_init(app)

    return app


def show_routers(app):
    from pprint import pprint as pp
    from operator import attrgetter
    rule_list = list(app.url_map.iter_rules())
    rule_list.sort(key=attrgetter('rule'))
    pp(rule_list)


def serve():
    app = init(settings)

    show_routers(app)

    app.run(host='0.0.0.0', port=3000)


if __name__ == '__main__':
    serve()