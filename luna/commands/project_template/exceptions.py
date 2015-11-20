# coding=utf8

"""
Copyright {{date().year}} {{project}}
"""

from webargs.flaskparser import parser


@parser.error_handler
def argerror_handler(e):
    raise Error(Error.ARGUMENT_ERROR, e.message)


class Error(Exception):
    """
    User custom error
    """
    " 0 ~ 1000 System Error "
    BOOTSTRAP_ERROR = 0
    ARGUMENT_ERROR = 1

    " 1000 ~ fin User Error "

    translate = {
        BOOTSTRAP_ERROR: u'System Internal Error',
        ARGUMENT_ERROR: u'Argument Error',
    }

    def __init__(self, code=0, message=""):
        self.error_code = code
        self.message = message or self.translate.get(self.error_code)

    def __str__(self):
        return self.message.encode('utf8')
