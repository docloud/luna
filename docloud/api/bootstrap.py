# coding=utf8

from webargs import Arg
from docloud.core import api

class Bootstrap(api.Api):
    router = 'bootstrap'

    @api.route('ping', methods=['GET'])
    def ping(self):
        return {'status': True}

