# coding=utf8

"""
Framework exceptions.
"""


class LunaException(Exception):
    """
    Base Exceptions, all exception raised by luna core base on it.
    """
    pass


class LoaderError(LunaException):
    """
    Loader error during loading.
    """
    pass


class ConfigLoadedError(LunaException):
    """
    Config can not be loaded.
    """
    pass


class ConfigSyntaxError(LunaException):
    """
    Error raise for invalid config syntax.
    """
    pass