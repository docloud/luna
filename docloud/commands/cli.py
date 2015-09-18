#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

import click

from docloud import server
from docloud.commands import shell as shell_module


@click.group(chain=True)
def cli():
    pass


@click.command()
def shell():
    shell_module.shell()


@click.command()
def serve():
    server.serve()


cli.add_command(shell)
cli.add_command(serve)