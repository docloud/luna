# coding=utf8

"""
Copyright 2015 Luna Project
"""

import re
import inspect
from webargs import fields
from flask.views import MethodView, http_method_funcs

ARGUMENT_PATTERN = re.compile(r'<>')


def get_args_by_rule(rule):
    pass


class Inspector(object):
    __inspected__ = None


class MethodViewInspector(Inspector):
    def __init__(self, view):
        self._view = view

    def get_view_funcs(self):
        all_members = inspect.getmembers(self._view)

        def is_api_view(func):
            if func.__name__ in http_method_funcs:
                return True
            if hasattr(func, 'rule'):
                return True
            return False

        return filter(is_api_view, all_members)
