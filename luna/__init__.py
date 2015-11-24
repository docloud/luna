# coding=utf8

"""
Copyright 2015 Luna project
"""


from flask import Flask
from flask.views import MethodView as View
from flask.ext.cache import Cache
from .config import ConfigManager


config_manager = ConfigManager()
config = config_manager.config
app = Flask(config["name"])
config_manager.init_app(app)
cache = Cache(app=app, with_jinja2_ext=False)
logger = app.logger
