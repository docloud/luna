# coding=utf8

from __future__ import absolute_import, division, print_function

from luna.api.bootstrap import Bootstrap

__all__ = [
    Bootstrap
]


def api_init(app):
    for dispatcher in __all__:
        dispatcher.register_app(app)

    return app
