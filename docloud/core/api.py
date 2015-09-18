# coding=utf8

from __future__ import absolute_import, division, print_function

import inspect
from flask import request, jsonify
from werkzeug.wrappers import Response

from flask.ext.login import (
    login_required
)
from flask.views import (
    MethodView,
    http_method_funcs
)

from webargs.flaskparser import use_args, parser


class Api(MethodView):
    """
    API Method View Class

    Usage:

        class(Api):
            def get(self):
                return {'status': True}

            @api.route('star')
            def book(self):
                return article.star()
    """
    router = None
    decorators = [] # Only use for method requests.
    api_decorators = []

    def dispatch_request(self, *args, **kwargs):
        """
        Dispatcher requests by method.
        """
        meth = getattr(self, request.method.lower(), None)
        # if the request method is HEAD and we don't have a handler for it
        # retry with GET
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        return self.execute_request(meth, *args, **kwargs)

    def execute_request(self, f, *args, **kwargs):
        f = self.auto_args(f)

        for decorator in self.api_decorators:
            f = decorator(f)

        data = f(*args, **kwargs)

        if isinstance(data, Response):
            return data

        resp = jsonify(data)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    def options(self):
        """
        Default handler for options method.

        Not implement RFC draft now.

        :return: the methods of this api supported.
        """
        implemented_methods = frozenset(self.__class__.__dict__.keys()).intersection(http_method_funcs)
        return {'methods': list(implemented_methods)}

    @classmethod
    def register_app(cls, app):
        rule = cls._build_api_rule()
        view = cls.as_view(cls.__name__)
        app.add_url_rule(rule, view_func=view)

        # Members only contain the Api class methods of use the route decorator.
        # Such as:
        #
        # @route('set', methods=('PUT'))
        # def set(self):
        #     return {'status': True}
        #
        members = inspect.getmembers(cls, predicate=lambda func: getattr(func, 'api', None))

        for name, member in members:
            func = cls.make_view_func(name)
            rule = cls._build_api_rule(rule=member.rule)
            options = member.options
            endpoint = '::'.join([cls.__name__, func.__name__])
            app.add_url_rule(rule, endpoint, func, **options)

    @classmethod
    def _build_api_rule(cls, rule=None, prefix='/api'):
        rules = [prefix, cls.router]
        if rule:
            rules.append(rule)
        return '/'.join(rules)

    @classmethod
    def make_view_func(cls, name, *class_args, **class_kwargs):
        """
        TODO: Parse the class_args/class_kwargs

        :param name:
        :param class_args:
        :param class_kwargs:
        :return:
        """
        def view_func(*args, **kwargs):
            self = view_func.view_class(*class_args, **class_kwargs)
            return self.execute_request(getattr(self, name), *args, **kwargs)

        view_func.view_class = cls
        view_func.__name__ = name
        view_func.__doc__ = cls.__doc__
        view_func.__module__ = cls.__module__
        view_func.methods = cls.methods
        return view_func

    def auto_args(self, f):
        name = f.__name__ + '_args'
        spec = getattr(self, name, None)
        if spec:
            return use_args(spec)(f)
        else:
            return f


def route(rule, **options):
    def decorator(f):
        f.api = True
        f.rule = rule
        f.options = options
        return f
    return decorator


@parser.error_handler
def webargs_error(e):
    raise Exception('qwe')