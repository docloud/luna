# coding=utf8

"""
Copyright {{date().year}} {{project}}
"""

from luna.models import db, rsdb

if rsdb:
    session = rsdb.session
    ModelBase = rsdb.Model