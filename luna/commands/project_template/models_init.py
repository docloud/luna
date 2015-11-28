# coding=utf8

"""
Copyright {{date().year}} {{project}}
"""

from luna.models import db, make_db_commit_decorator

mysql = db.get("mysql")
engine = mysql.get("engine")
Session = mysql.get("session")
ModelBase = mysql.get("base")

auto_commit = make_db_commit_decorator(Session, Error, Error.DATABASE_ERROR)