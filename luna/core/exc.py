# coding=utf8

from flask import jsonify
from webargs.core import WebargsError
from webargs.flaskparser import parser
from luna.settings.exceptions import ErrorCode, TranslateCode


# TODO: Correct the http code base on RFC documents.

BAD_REQUEST = 400
SERVER_ERROR = 500
REJECT_ERROR = 403


class BaseException(Exception):
    code = 0
    message = "BaseException"

    def jsonify(self):
        return jsonify({'code': self.code, 'message': self.message})


class UserException(BaseException):
    def __init__(self, code, message=None):
        self.code = code
        self.message = message or TranslateCode(code) or '逻辑异常'


class SystemException(BaseException):
    def __init__(self, code, message=None):
        self.code = code
        self.message = message or TranslateCode(code) or '系统异常'


class UnknownException(BaseException):
    def __init__(self, e):
        self.code = REJECT_ERROR
        self.message = e.message or '未知异常'


def exc_init(app):
    @app.errorhandler(Exception)
    def errorhandler(e):
        app.logger.exception(e)
        if isinstance(e, SystemException):
            return e.jsonify(), SERVER_ERROR
        if isinstance(e, UserException):
            return e.jsonify(), 406
        if isinstance(e, WebargsError):
            return UserException(ErrorCode.ARGS_PARSED_ERROR, e.message).jsonify(), BAD_REQUEST
        else:
            return UnknownException(e).jsonify(), REJECT_ERROR

    @app.errorhandler(404)
    def page_not_found(e):
        return SystemException(ErrorCode.PAGE_NOT_FOUND).jsonify(), 404

    @app.errorhandler(401)
    def unauthorization(e):
        return SystemException(ErrorCode.UNAUTH).jsonify(), 401

    @parser.error_handler
    def webargs_error(e):
        raise
