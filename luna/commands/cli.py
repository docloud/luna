# coding=utf8

import click

from .bootstrap import init_project
from ..init import run_app


@click.group(chain=True)
def cli():
    pass


@click.command('init')
@click.argument('name')
def init(name):
    init_project(name)


@click.command('shell')
def start_shell():
    from luna import app, config, logger
    from luna.clients import http
    from IPython import embed
    embed()


@click.command('serve')
def start_server():
    from imp import load_package
    from luna import config, logger
    name, app_config = config["name"], config["app"]
    if name != "default":
        load_package(name, name)
    logger.info("Server starting on http://{host}:{port}".format(**app_config))
    run_app()


cli.add_command(init)
cli.add_command(start_shell)
cli.add_command(start_server)
