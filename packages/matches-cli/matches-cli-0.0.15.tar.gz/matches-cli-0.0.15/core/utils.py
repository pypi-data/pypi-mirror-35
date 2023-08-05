
# -*- coding:utf-8 -*-
import subprocess
import click
import os


def get_shell_config():
    """
    获取用户当前使用的Shell的配置文件
    :return: 返回配置文件路径
    """
    shell = os.environ.get('SHELL')
    if shell == '/bin/zsh':
        shell_config = '~/.zshrc'
    elif shell == '/bin/bash':
        shell_config = '~/.bash_profile'
    else:
        shell_config = click.prompt('无法识别当前shell的配置文件，请输入配置文件路径')
    return os.path.expanduser(shell_config)


def command_exists(cmd):
    """
    用于判断当前命令是否存在
    :param cmd: 命令名称
    :return: True or False
    """
    try:
        exitcode, _ = subprocess.getstatusoutput("command -v %s >/dev/null 2>&1" % cmd)
    except AttributeError:
        import commands
        exitcode, _ = commands.getstatusoutput("command -v %s >/dev/null 2>&1" % cmd)
    return exitcode == 0


def execute_shell(cmd):
    """
    执行shell命令
    :param cmd: string， shell命令
    :return: True执行成功，False失败
    """
    return subprocess.call(cmd, shell=True) == 0


def get_shell_result(cmd):
    try:
        exitcode, data = subprocess.getstatusoutput(cmd)
    except AttributeError:
        import commands
        exitcode, data = commands.getstatusoutput(cmd)
    if exitcode == 0:
        return data
    else:
        return None
