# coding=utf8

"""
Copyright {{date().year}} {{project}}
"""

from luna.models import db

mysql = db.get("mysql")
engine = mysql.get("engine")
Session = mysql.get("session")
ModelBase = mysql.get("base")