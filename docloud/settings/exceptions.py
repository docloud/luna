# coding=utf8

"""
Configure the exceptions at here.
"""


class ErrorCode(object):
    " 0 ~ 1000 System Error "
    PAGE_NOT_FOUND = 404

    ARGS_PARSED_ERROR = 800


class TranslateCode(object):
    translate = {
        ErrorCode.PAGE_NOT_FOUND: 'Page Not Found',
    }

    def __init__(self, code):
        pass

    def __new__(self, code):
        return self.translate.get(code, None)
