#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

import click

from luna.core import server
from luna.commands import shell as shell_module


@click.group(chain=True)
def cli():
    pass


@click.command()
def shell():
    shell_module.shell()


@click.command('serve')
def start_server():
    server.serve()


cli.add_command(shell)
cli.add_command(start_server)
