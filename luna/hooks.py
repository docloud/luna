# coding=utf8

"""
Copyright 2015 Luna Project
"""


class HooksManager(object):
    def __init__(self):
        self._hooks = {}

    def __dir__(self):
        return self._hooks.keys()

    def add_hook(self, key, func):
        self._hooks[key] = func

    def get_hook(self, key):
        return self._hooks[key]


hooks_manager = HooksManager()


def hook(func):
    hooks_manager.add_hook(func.__name__, func)
    return func


@hook
def api_loader():
    return []
