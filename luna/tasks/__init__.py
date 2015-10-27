# coding=utf8

import celery

celery_app = celery.Celery(broker='redis://localhost:6379/0', backend='redis')

from . import *