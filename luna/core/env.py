# coding=utf8

import os


def is_dev_environ():
    return not os.environ.get('deploy_machine', False) == 'develop'
