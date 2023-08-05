
# -*- coding:utf-8 -*-
import click
import subprocess

from core import env as env_helper
from core import version
from core import utils

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Matches version: ' + version.__version__)
    click.echo('Wax version: ' + utils.get_shell_result('wax -v'))
    ctx.exit()


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--version', is_flag=True, callback=print_version,
              is_eager=True, expose_value=False, help='显示版本信息')
def matches():
    pass


@matches.command(context_settings=CONTEXT_SETTINGS)
def init():
    """
    初始化 wax 工程
    """
    subprocess.call('wax init', shell=True)


@matches.command(context_settings=CONTEXT_SETTINGS)
@click.option('-b', '--boilerplate', nargs=1, type=str, help='指定运行自定义命令的模版')
@click.option('-a', '--all', is_flag=True, help='指定所有模版，没定义则跳过')
@click.option('-A', '--all-exit-error', is_flag=True, help='指定所有模版，没定义则退出并抛错')
@click.option('-t', '--test-wax', is_flag=True, help='从 wax 测试源获取依赖信息')
@click.option('-x', '--test-registry', is_flag=True, help='使用测试源模版')
@click.option('-l', '--local-boilerplate', is_flag=True, help='使用本地模版，一般用于模版开发自测')
@click.option('-d', is_flag=True, help='显示详细的 debug 信息')
@click.argument('arg', nargs=-1)
def run(arg, boilerplate, all, all_exit_error, test_wax, test_registry, local_boilerplate, d):
    """
    运行模板的自定义命令
    """
    option_a = '-a' if all else ''
    option_b = '-b ' + boilerplate if boilerplate else ''
    option_A = '-A' if all_exit_error else ''
    option_t = '-t' if test_wax else ''
    option_x = '-x' if test_registry else ''
    option_l = '-l' if local_boilerplate else ''
    option_d = '-d' if d else ''
    argument = arg[0] if arg else ''

    subprocess.call(
        'wax run {cmd} {option_a} {option_b} {option_A} {option_t} {option_x} {option_l} {option_d}'.format(
            cmd=argument,
            option_a=option_a,
            option_A=option_A,
            option_b=option_b,
            option_t=option_t,
            option_x=option_x,
            option_l=option_l,
            option_d=option_d
        ), shell=True)


@matches.command(context_settings=CONTEXT_SETTINGS)
@click.option('--env', nargs=1, type=click.Choice(['android', 'ios', 'wax', 'all', 'android_studio', 'xcode']),
              help='安装开发环境')
@click.option('-d', is_flag=True, help='显示详细的 debug 信息')
def install(env, d):
    """
    安装wax开发环境、安装 wax 项目用到的模版及依赖
    """
    if env:
        env_helper.env_install(env)
        return

    option_d = '-d' if d else ''
    subprocess.call('wax install {option_d}'.format(option_d=option_d), shell=True)


@matches.command(context_settings=CONTEXT_SETTINGS)
@click.option('-d', is_flag=True, help='显示详细的 debug 信息')
@click.option('-b', '--boilerplate', nargs=1, type=str, help='指定运行自定义命令的模版')
@click.option('-t', '--test-wax', is_flag=True, help='从 wax 测试源获取依赖信息')
@click.argument('arg', nargs=-1)
def add(d, boilerplate, test_wax, arg):
    """
    添加模版或 wax 依赖
    """
    option_d = '-d' if d else ''
    option_b = '-b ' + boilerplate if boilerplate else ''
    option_t = '-t' if test_wax else ''
    cmd = arg[0] if arg else ''
    subprocess.call(
        'wax add {cmd} {option_d} {option_b} {option_t}'.format(
            cmd=cmd,
            option_d=option_d,
            option_b=option_b,
            option_t=option_t), shell=True)


@matches.command(context_settings=CONTEXT_SETTINGS)
@click.option('-d', is_flag=True, help='显示详细的 debug 信息')
@click.option('-b', '--boilerplate', nargs=1, type=str, help='指定运行自定义命令的模版')
@click.option('-t', '--test-wax', is_flag=True, help='从 wax 测试源获取依赖信息')
@click.argument('args', nargs=-1)
def update(d, test_wax, arg, boilerplate):
    """
    添加模版或 wax 依赖
    """
    option_d = '-d' if d else ''
    option_b = '-b ' + boilerplate if boilerplate else ''
    option_t = '-t' if test_wax else ''
    cmd = arg[0] if arg else ''
    subprocess.call(
        'wax update {cmd} {option_d} {option_b} {option_t}'.format(
            cmd=cmd,
            option_d=option_d,
            option_b=option_b,
            option_t=option_t), shell=True)





