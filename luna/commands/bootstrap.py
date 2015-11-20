# coding=utf8

"""
A Tools for generate and validate container.
"""

import os
from os.path import join
from datetime import datetime
from werkzeug.security import gen_salt
from toolkit.tpl import render, env
from luna import app, config, logger


def copy(source, dest, context=None):
    logger.info(dest)
    current_dirname = os.path.dirname(os.path.abspath(__file__))
    return render(
        join(current_dirname, 'project_template', source),
        join(config["name"], dest),
        **(context or {})
    )


def mkdirify(path):
    if os.path.exists(path):
        logger.error('The folder {} has been existed.'.format(path))
    else:
        os.makedirs(path)


def init_project(name):
    logger.info('Building ...')

    context = {
        "project": name
    }

    env.globals["date"] = lambda : datetime.now()
    env.globals["gen_salt"] = gen_salt

    config["name"] = name
    mkdirify(name)

    # Project files.
    mkdirify(join(name, name))
    copy('app.yaml', 'app.yaml', context)
    copy('Makefile', 'Makefile', context)
    copy('setup.py', 'setup.py', context)
    copy('requirements.txt', 'requirements.txt', context)
    copy('hook_init.py', join(name, '__init__.py'), context)
    copy('exceptions.py', join(name, 'exceptions.py'), context)

    # Generate API files.
    mkdirify(join(name, name, "api"))
    copy('api_init.py', join(name, 'api', '__init__.py'), context)

    # DB Connector files.
    mkdirify(join(name, name, "models"))
    copy('models_init.py', join(name, 'models', '__init__.py'), context)