#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Flask
from luna import settings
from luna.api import api_init
from luna.core.logger import logger_init
from luna.core.auth import auth_init
from luna.core.db import db_init
from luna.core.exc import exc_init


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
    global app
    show_routers(app)
    app.run(host=app.config['HOST'], port=app.config['PORT'])


app = init(settings)

if __name__ == '__main__':
    serve()
