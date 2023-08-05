
# -*- coding:utf-8 -*-
import click

def info(message):
    click.echo('[info]  {msg}'.format(msg=message))


def error(msg):
    click.echo('\033[0;31m[error]  {msg}\033[0m'.format(msg=msg))


def success(msg):
    click.echo('\033[0;33m[success] {msg}\033[0m'.format(msg=msg))


def tips(msg):
    click.echo('\033[0;36m[tips]  {msg}\033[0m'.format(msg=msg))
