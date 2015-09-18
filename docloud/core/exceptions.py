# coding=utf8


class UserException(Exception):
    def __init__(self, code, msg=None):
        pass


class SystemException(Exception):
    def __init__(self, e):
        pass 