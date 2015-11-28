# coding=utf8

import click
from fabric.api import (
    run,
    env,
    cd
)
from fabric.contrib.project import rsync_project

from .. import app, config, logger, cache
from .bootstrap import init_project
from ..init import run_app


@click.group(chain=True)
def cli():
    pass


@click.command('init')
@click.argument('name')
def init(name):
    """
    Init service
    """
    init_project(name, license="mit")


@click.command('shell')
def start_shell():
    """
    Start shell
    """
    from luna.clients import http
    from IPython import embed
    embed()


@click.command('serve')
def start_server():
    """
    Start server
    """
    from imp import load_package
    name, host, port = app.name, app.config["HOST"], app.config["PORT"]
    if name != "default":
        load_package(name, name)
    logger.info("Server starting on http://{}:{}".format(host, port))
    run_app()

@click.command('upload')
@click.argument('source')
@click.argument('dest')
@click.option('--user', default="runner", help="user")
@click.option('--host', default=config["deploy"]["host"], help="host")
def upload_files(source, dest, user, host):
    """
    Upload files
    """
    env.user = user
    env.host_string = host
    env.use_ssh_config = True

    rsync_project(local_dir=source, remote_dir=dest, exclude=(".git", ".idea"))


@click.command('deploy')
@click.option('--user', default="runner", help="user")
@click.option('--host', default=config["deploy"]["host"], help="host")
def deploy(user, host):
    """
    Deploy service
    """
    env.user = user
    env.host_string = host
    env.use_ssh_config = True

    name = config['name']
    remote_dir = "/srv/{}".format(name)
    rsync_project(local_dir=".", remote_dir=remote_dir, exclude=(".git", ".idea", "node_modules"))
    with cd(remote_dir):
        run("sudo /srv/venv/luna/bin/pip install .".format(name))
        run("sudo supervisorctl restart {}".format(name))


cli.add_command(init)
cli.add_command(start_shell)
cli.add_command(start_server)
cli.add_command(upload_files)
cli.add_command(deploy)
