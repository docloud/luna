# coding=utf8

from contextlib import contextmanager
from fabric.api import (
    run,
    local,
    env,
    task,
    put
)
