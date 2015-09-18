# coding=utf8

from contextlib import contextmanager
from fabric.api import (
    run,
    local,
    env,
    task,
    put
)
from ops import (
    develop,
    ops
)
from ops.ping import *

@task
def docloud():
    """
    Demo deploy
    """
    with develop():
        put('docs/technology/build/html/*', '/data/docs/docloud/')
