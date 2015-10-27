# coding=utf8

import requests
from luna import settings
from luna.clients import logger


def switch_user(user, password):
    login_url = 'https://{HOST}/sso/login'.format(**settings.basic.__dict__)
    response = requests.post(login_url, json={'username': user, 'password': password})
    try:
        token = response.json()['token']
    except Exception as e:
        logger.warn('登录失效, 请重新登录, {}'.format(e.message))


class User(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        return switch_user(item, 'zxc123')
