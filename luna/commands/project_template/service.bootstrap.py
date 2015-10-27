# coding=utf8

from luna.core.service import Service


class Bootstrap(Service):
    def ping(self):
        return {'status': True}