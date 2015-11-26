# coding=utf8

import click
from fabric.api import (
    run,
    env,
    cd
)
from fabric.contrib.project import rsync_project

from .bootstrap import init_project
from ..init import run_app


@click.group(chain=True)
def cli():
    pass


@click.command('init')
@click.argument('name')
def init(name):
    init_project(name, license="mit")


@click.command('shell')
def start_shell():
    from luna import app, config, logger, cache
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

@click.command('upload')
@click.argument('source')
@click.argument('dest')
def upload_files(source, dest):
    from luna import config
    env.user = "runner"
    env.host_string = config["deploy"]["host"]
    env.use_ssh_config = True

    rsync_project(local_dir=source, remote_dir=dest, exclude=(".git", ".idea"))


@click.command('deploy')
def deploy():
    from luna import config
    env.user = "runner"
    env.host_string = config["deploy"]["host"]
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
