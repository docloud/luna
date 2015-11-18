# coding=utf8

"""
Copyright 2015 Luna project
"""


from flask import Flask
from .config import DefaultConfig


config = DefaultConfig.load()
app = Flask(config["name"])
app.config.update(config["app"])
logger = app.logger
