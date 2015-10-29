#!/usr/bin/env python
# coding=utf8

from __future__ import absolute_import, division, print_function

import click

from luna.core import serve
from luna.commands import shell as shell_module


@click.group(chain=True)
def cli():
    pass


@click.command()
def shell():
    shell_module.shell()


@click.command()
def serve():
    serve.serve()


cli.add_command(shell)
cli.add_command(serve)
