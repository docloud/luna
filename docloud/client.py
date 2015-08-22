#coding=utf8

from __future__ import print_function, division, absolute_import
import IPython
import requests
import config
import logging
from docloud.core.log import logger_init

logger_init()
log = logging.getLogger('console')


def switch_user(user, password):
    login_url = 'https://{HOST}/sso/login'.format(**config.__dict__)
    response = requests.post(login_url, json={'username': user, 'password': password})
    try:
        token = response.json()['token']
    except Exception as e:
        log.warn('登录失效, 请重新登录, {}'.format(e.message))


class User(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        return switch_user(item, 'zxc123')


if __name__ == '__main__':
    user = User()
    IPython.embed()
