# coding=utf8

from __future__ import absolute_import, division, print_function

import os


def is_dev_environ():
    return os.environ.get('docloud_mode', False) == 'develop'