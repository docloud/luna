# coding=utf8

from contextlib import contextmanager
from fabric.api import (
    run,
    local,
    env,
    task
)


class Environ(object):
    sso_host = '123.59.50.131'
    sso_port = 8000
    backend_host = '123.59.50.131'
    backend_port = 3000


@contextmanager
def develop():
    env.use_ssh_config = True
    env.host_string = 'docloud'
    yield


@contextmanager
def ops():
    env.use_ssh_config = True
    env.host_string = 'docloud'
    yield
