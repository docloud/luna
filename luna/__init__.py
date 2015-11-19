# coding=utf8

"""
Copyright 2015 Luna project
"""


from flask import Flask
from flask.views import MethodView as View
from .config import DefaultConfig


config = DefaultConfig.load()
app = Flask(config["name"])
app.config.update(config["app"])
logger = app.logger

import logging
logger = logging.getLogger("demo")
logger.info("acvbnm")