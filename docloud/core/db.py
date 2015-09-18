# coding=utf8

from __future__ import absolute_import, division, print_function

from mongoengine import connect


def mongo_connect(config):
    """
    Re-use the mongo connection

    :param config: config for mongo connection
    :return: None
    """
    if config:
        connect('docloud', host=config['conn'])


def db_init(db_settings):
    mongo_connect(db_settings.get('MONGODB'))