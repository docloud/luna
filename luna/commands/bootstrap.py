# coding=utf8

"""
A Tools for generate and validate container.
"""

import os
from os.path import join
from datetime import datetime
from toolkit.tpl import render, register_func
from luna import app, config, logger


def copy(source, dest):
    logger.info(dest)
    return render(
        join('project_template', source),
        join(config.name, dest)
    )


def init_project(name):
    logger.info('Building ...')

    register_func('date', datetime.date)

    config.name = name
    if os.path.exists(name):
        logger.error('The folder {} has been existed.'.format(name))
    os.makedirs(name)

    # Project files.
    copy('Makefile', 'Makefile')
    copy('requirements.txt', 'requirements.txt')
    copy('__init__.py', join(name, '__init__.py'))

    # Generate API files.
    copy('__init__.py', join(name, 'api', '__init__.py'))
    copy('bootstrap.py', join(name, 'api', 'bootstrap.py'))
