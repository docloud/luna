# coding=utf8

from mongoengine import connect
from luna.core.config import config


def mongo_connect(config):
    """
    Re-use the mongo connection

    :param config: config for mongo connection
    :return: None
    """
    if config:
        connect('luna', host=config['conn'])


def db_init(app):
    pass