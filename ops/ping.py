# coding=utf8

from fabric.api import (
    task,
    run
)
from . import develop


@task
def ping():
    """
    检测服务的有效性
    """
    with develop():
        run('ls -al')
