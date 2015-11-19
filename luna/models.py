# coding=utf8

"""
Copyright 2015 Luna Project
"""

from six import iteritems
from luna import config, logger
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DBManager(object):
    def __init__(self, config, pool_size=10, create_session=True):
        """Create databases from config

        :param config: config list that contain dictionary like:

            [
                {
                    "alias": "mysql", // or mongodb
                    "host": "127.0.0.1",
                    "port": 3306,
                    "database": "demo"
                }
            ]

        :param pool_size: connection pool size
        :param create_session: auto create session during instance created.
        :return: database object in this instance.

            SQL Database:

            {
                "engine": <...>, // engine created by :func:`create_engine`
                "base": <...>, // model base created by :func:`declarative_base`
                "session": <...> //connection session created by :func:`sessionmaker`
            }

            MongoDB Database:

            {
                "client": <...>, // client breated by :class:`MongoClient`
                "database": <...> // database connection pool created by client *attribute getter*
            }
        """
        self.db_pool_managers = {}
        self.db_map = {}
        self.config = config
        self.pool_size = pool_size
        self.create_pool_managers()
        if create_session:
            self.create_sessions()

    def create_pool_managers(self):
        for name, database in iteritems(self.config):
            alias = database["alias"]
            alias_creator = getattr(self, "alias_" + alias, None)
            self.db_pool_managers[name] = lambda: alias_creator(database)

    def create_sessions(self):
        for name, creator in iteritems(self.db_pool_managers):
            self.db_map[name] = creator()

    def get(self, item):
        return self.db_map.get(item)

    def get_pool_manager(self, item):
        return self.db_pool_managers.get(item)

    def alias_mysql(self, mysql_config):
        conn_descriptor = "mysql://{username}:{password}@{host}:{port}/{database}".format(**mysql_config)
        # There is a connection pool in engine
        engine = create_engine(conn_descriptor)
        ModelBase = declarative_base(bind=engine)
        Session = sessionmaker(bind=engine)
        return {
            "engine": engine,
            "base": ModelBase,
            "session": Session
        }

    def alias_mongodb(self, mongodb_config):
        mongodb_config.setdefault('maxPoolsize',
                                  mongodb_config.get('pool_size') or self.pool_size)
        client = MongoClient(**mongodb_config)
        database = getattr(client, mongodb_config["database"], None)
        return {
            "client": client,
            "database": database
        }


db = DBManager(config=config["databases"])
