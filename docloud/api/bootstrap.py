# coding=utf8

from webargs import Arg
from docloud.core import api
from docloud.services import bootstrap
from flask import make_response
import jsonpickle


class Bootstrap(api.Api):
    router = 'bootstrap'
    service = bootstrap.Bootstrap()

    ping_x_args = {
        'name': Arg(str, required=True)
    }

    @api.route('ping', methods=['GET'])
    def ping(self):
        return self.service.ping()

    @api.route('ping_x')
    def ping_x(self, args):
        return args