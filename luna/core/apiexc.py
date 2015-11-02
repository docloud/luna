# coding=utf8

"""
Handle API Exceptions
"""

from flask import jsonify
from webargs.core import WebargsError
from webargs.flaskparser import parser
from luna import loader, logger

# TODO: Correct the http code base on RFC documents.

BAD_REQUEST = 400
SERVER_ERROR = 500
REJECT_ERROR = 403
UNPROCESSABLE_ENTITY = 422


class ArgumentError(WebargsError):
    http_code = UNPROCESSABLE_ENTITY

    def __init__(self, e):
        self.e = e
        self.http_code = getattr(e, 'status_code', UNPROCESSABLE_ENTITY)
        self._message = getattr(e, 'message', None) or 'Validate Error'

    @property
    def message(self):
        return jsonify(
            error=self.e.__class__.__name__,
            categoty=self.__class__.__name__,
            http_code=self.http_code,
            message=self._message
        )


class UnknownException(Exception):
    http_code = SERVER_ERROR

    def __init__(self, e):
        self.e = e
        self._message = getattr(e, 'message', None) or 'UnknownException'

    @property
    def message(self):
        return jsonify(
            error=self.e.__class__.__name__,
            categoty=self.__class__.__name__,
            http_code=self.http_code,
            message=self._message
        )


def exc_init(app):
    exceptions = loader.load_project_exc()
    exceptions.extend([
        ArgumentError,
        UnknownException
    ])

    @app.errorhandler(Exception)
    def errorhandler(e):
        logger.exception(e)
        for exception in exceptions:
            if isinstance(e, exception):
                return e.message, e.http_code
        else:
            err = UnknownException(e)
            return err.message, err.http_code

    @app.errorhandler(404)
    def page_not_found(e):
        logger.exception(e)
        return jsonify(
            error=None,
            category=None,
            http_code=404,
            message='Page not found'
        ), 404

    @app.errorhandler(401)
    def unauthorization(e):
        logger.exception(e)
        return jsonify(
            error=None,
            category=None,
            http_code=401,
            message='Unauthorization'
        ), 401

    @parser.error_handler
    def webargs_error(e):
        logger.exception(e)
        if isinstance(e, WebargsError):
            raise ArgumentError(e)
        else:
            raise e
