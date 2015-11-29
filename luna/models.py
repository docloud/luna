# coding=utf8

"""
Copyright 2015 Luna Project
"""

from six import iteritems
from luna import app, config, logger
from pymongo import MongoClient
from flask.ext.sqlalchemy import SQLAlchemy


class DBManager(object):
    def __init__(self, config=None, app=None):
        """ Create databases from config """
        self.app = app
        self.config = config or {}
        self.rsdb = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        sqlalchemy_binds = {}

        for name, database in iteritems(self.config):
            dialect = database.get("dialect")
            if dialect in ("mysql", ):
                database.setdefault("username", "root")
                database.setdefault("password", "")
                database.setdefault("charset", "utf8")
                uri = ("mysql://{username}:{password}@{host}:{port}/{database}"
                       "?charset=utf8mb4").format(**database)
                sqlalchemy_binds[name] = uri

        if len(sqlalchemy_binds) == 1:
            app.config.update({
                "SQLALCHEMY_DATABASE_URI": sqlalchemy_binds.values()[0]
            })
        if len(sqlalchemy_binds) > 1:
            app.config.update({
                "SQLALCHEMY_BINDS": {name: value for name, value in
                                     iteritems(sqlalchemy_binds)[1:]}
            })
        if sqlalchemy_binds:
            app.config.update({
                "SQLALCHEMY_TRACK_MODIFICATIONS": True
            })
            self.rsdb = SQLAlchemy(app)


    def alias_mongodb(self, mongodb_config):
        mongodb_config.setdefault('maxPoolsize',
                                  mongodb_config.get('pool_size') or self.pool_size)
        client = MongoClient(**mongodb_config)
        database = getattr(client, mongodb_config["database"], None)
        return {
            "client": client,
            "database": database
        }


def _serialize(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def serialize(obj):
    if isinstance(obj, list):
        return map(_serialize, obj)
    return _serialize(obj)


db = DBManager(config=config["databases"])
db.init_app(app)
rsdb = db.rsdb