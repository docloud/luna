# coding=utf8

"""
Copyright {{date().year}} {{project}}
"""

from luna.hooks import hook


@hook
def api_loader():
    from .api import __all__

    return __all__
