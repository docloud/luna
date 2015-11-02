#!/usr/bin/env python
# coding=utf8

from flask import Flask
from luna.core.logger import logger_init
from luna.core.auth import auth_init
from luna.core.db import db_init
from luna.core.config import config
from luna.core.apiexc import exc_init
from luna import loader


def api_init(app, apis):
    for dispatcher in apis:
        dispatcher.register_app(app)

    return app


def init_app():
    app = Flask(__name__)
    app.config.update({'luna': config})

    apis = loader.load_project_api()
    api_init(app, apis)

    logger_init(app)
    auth_init(app)
    db_init(app)
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
    app.run(host=config.app['host'], port=config.app['port'])


app = init_app()