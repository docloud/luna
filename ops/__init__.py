# coding=utf8

from contextlib import contextmanager
from fabric.api import (
    run,
    local,
    env,
    task
)


@contextmanager
def develop():
    env.use_ssh_config = True
    env.host_string = 'docloud'
    yield


@contextmanager
def ops():
    env.use_ssh_config = True
    yield
