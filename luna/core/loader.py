# coding=utf8

import os
import imp
import inspect
from .config import config
from .api import Api


def load_project_module(path=None):
    if not path:
        path = config.name
    else:
        path = os.path.join(config.name, path)
    return imp.load_source(config.name, path)


def load_project_exc(path=None):
    if not path:
        path = os.path.join(config.name, 'exceptions.py')
    else:
        path = os.path.join(config.name, path)
    module = imp.load_source(config.name, path)
    exceptions = [
        cls for cls in module.__dict__.values()
        if inspect.isclass(cls) and issubclass(cls, Exception) and \
        hasattr(cls, 'http_code') and hasattr(cls, 'message')
        ]
    return exceptions


def load_project_api(path=None):
    if not path:
        path = os.path.join(config.name, 'api')
    else:
        path = os.path.join(config.name, path)

    apis = []
    all_module = [
        p for p in os.listdir(path)
        if '__' not in p and p.endswith('.py')
        ]
    for module_name in all_module:
        module = imp.load_source(module_name[0:-3], os.path.join(path, module_name))
        all_class = [
            cls for cls in module.__dict__.values()
            if inspect.isclass(cls) and issubclass(cls, Api)
        ]
        apis.extend(all_class)
    return apis
