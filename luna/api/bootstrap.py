# coding=utf8

from webargs import Arg
from luna.core import api
from luna.services import bootstrap
from luna.settings.exceptions import ErrorCode
from luna.core.exc import UserException


class Bootstrap(api.Api):
    router = 'bootstrap'
    service = bootstrap.Bootstrap()

    ping_x_args = {
        'name': Arg(int, required=True)
    }

    @api.route('ping', methods=['GET'])
    def ping(self):
        return self.service.ping()

    @api.route('ping_x')
    def ping_x(self, args):
        return args
