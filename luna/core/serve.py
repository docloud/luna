#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

import os
from flask import Flask
from luna import config
from luna.core.api import Api
from luna.core.logger import logger_init
from luna.core.auth import auth_init
from luna.core.db import db_init
from luna.core.exc import exc_init


def api_init(app, apis):
    for dispatcher in apis:
        dispatcher.register_app(app)

    return app


def dynamic_load_apis():
    for module in os.walk('api'):
        print(module)


def init(settings):
    app = Flask(__name__)

    app.config.update(config)

    apis = dynamic_load_apis()
    api_init(app, apis)

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