# -*- coding:utf-8 -*-
import shutil
import zipfile
from contextlib import closing
import requests
import re
import os
import click

from tqdm import tqdm

from core import utils, console

HOME = os.environ.get('HOME')
ZSH = "/bin/zsh"
BASH = "/bin/bash"
ZSHRC = HOME + '/.zshrc'
BASH_PROFILE = HOME + '/.bash_profile'
ANDROID_SDK_DIR = HOME + '/Library/Android/sdk'
ANDROID_SDK_MANAGER = ANDROID_SDK_DIR + '/tools/bin/sdkmanager'
ANDROID_STUDIO_DMG = HOME + '/Downloads/android_studio.dmg'
ANDROID_TOOLS_ZIP = HOME + '/Downloads/android_tools.zip'
GRADLE_DIR = HOME + '/Documents/gradle'
GRADLE = GRADLE_DIR + '/gradle-3.3'
GRADLE_ZIP = HOME + '/Downloads/gradle-3.3-all.zip'


def _brew():
    if utils.command_exists('brew'):
        return True

    if utils.execute_shell(
            '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'):
        if utils.command_exists('brew'):
            console.success('Brew安装成功')
            return True

    console.error('Brew安装失败')
    return False


def _android(shell_config):
    android_home = os.environ.get('ANDROID_HOME') if os.environ.get('ANDROID_HOME') else ''
    if android_home and utils.command_exists('adb'):
        console.tips('已配置Android环境')
        return True

    if not utils.command_exists('gradle'):
        _gradle(shell_config)

    insert_cmd = r"sed -i '' '/^export PATH/i \
    export ANDROID_HOME=${{HOME}}/Library/Android/sdk \
    ' {shell_config}"
    replace_cmd = r"sed -i '' 's/^\(export PATH=\)\(.*\)/\1\2:$ANDROID_HOME\/platform-tools:$ANDROID_HOME\/tools\/bin/' {shell_config}"

    if _exist_android_core_file():
        if not android_home:
            utils.execute_shell(insert_cmd.format(shell_config=shell_config))
        if (not android_home) or (android_home not in os.environ.get('PATH')):
            utils.execute_shell(replace_cmd.format(shell_config=shell_config))
        console.success('Android环境配置成功')
        return True
    else:
        if _android_tools():
            utils.execute_shell('sh {sdkmanager} --licenses'.format(sdkmanager=ANDROID_SDK_MANAGER))
            packages = ['build-tools;26.0.2', 'platforms;android-26', 'platforms;android-16', 'platforms;android-22',
                        'platforms;android-19', 'platform-tools', 'extras;android;m2repository']
            for package in packages:
                utils.execute_shell(
                    'sh {sdkmanager} "{package}" --no_https --proxy=http --proxy_host=g.cn --proxy_port=80'.format(
                        sdkmanager=ANDROID_SDK_MANAGER, package=package))
            if not android_home:
                utils.execute_shell(insert_cmd.format(shell_config=shell_config))
            if (not android_home) or (android_home not in os.environ.get('PATH')):
                utils.execute_shell(replace_cmd.format(shell_config=shell_config))
            if _exist_android_core_file():
                console.success('android环境配置成功')
                return True

    console.error('Android环境配置失败')
    return False


def _exist_android_core_file():
    core_dir_set = {'platform-tools', 'tools', 'build-tools', 'platforms', 'extras'}
    try:
        return os.path.exists(ANDROID_SDK_DIR) and core_dir_set.issubset(os.listdir(ANDROID_SDK_DIR))
    except:
        return False


def _android_tools():
    if os.path.exists(ANDROID_SDK_MANAGER):
        console.tips('已安装Android命令行工具')
        return True

    download_url = _get_download_url(
        'https://developer.android.google.cn/studio/',
        'href="(https://dl\.google\.com/android/repository/sdk-tools-darwin-[0-9]+\.zip)"')
    if download_url:
        if _download_file(url=download_url,
                          dst=ANDROID_TOOLS_ZIP,
                          tips='downloading android tools'):
            # shutil.unpack_archive(os.path.expanduser(ANDROID_TOOLS_ZIP), os.path.expanduser(ANDROID_SDK_DIR))
            zip = zipfile.ZipFile(ANDROID_TOOLS_ZIP)
            zip.extractall(ANDROID_SDK_DIR)
            if os.path.exists(ANDROID_SDK_MANAGER):
                console.success('Android命令行工具下载成功')
                return True
    console.error('Android命令行工具下载失败')
    return False


def _node(shell_config):
    if utils.command_exists('node'):
        console.tips('已安装Node')
        return True

    if _n():
        utils.execute_shell('source {shell_config} && n lts'.format(shell_config=shell_config))
        if utils.command_exists('node'):
            console.success('Node安装成功')
            return True

    console.error('Node安装失败')
    return False


def _download_file(url, dst, tips):
    dst = os.path.expanduser(dst)
    if os.path.exists(dst):
        cur_size = os.path.getsize(dst)
    else:
        cur_size = 0

    headers = {'Range': 'bytes={cur_size}-'.format(cur_size=cur_size)}
    try:
        with closing(requests.get(url, headers=headers, stream=True)) as response:
            file_size = int(response.headers.get('content-length', 0)) + cur_size
            progress = tqdm(total=file_size, initial=cur_size, unit='B', unit_scale=True, desc=tips)
            with open(dst, 'ab') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        progress.update(1024)
                progress.close()
        return True
    except Exception as e:
        console.error(e)
        return False


def _android_studio():
    if os.path.exists('/Applications/Android Studio.app'):
        console.tips('已安装Android Studio')
        return True

    choice = click.prompt('是否下载Android Studio？', default='y')
    if choice.lower() == 'y':
        download_url = _get_download_url(
            'https://developer.android.google.cn/studio/',
            'href="(https://dl\.google\.com/dl/android/studio/install/[0-9.]+/android-studio-ide-[0-9.]+-mac\.dmg)"')
        if download_url:
            if _download_file(url=download_url,
                              dst=ANDROID_STUDIO_DMG,
                              tips='downloading android-studio'):
                # 挂载DMG
                utils.execute_shell('hdiutil attach -quiet {dir}'.format(dir=ANDROID_STUDIO_DMG))
                app_dir = '/Volumes/' + utils.get_shell_result("ls /Volumes | grep 'Android Studio.*'")
                app = app_dir + "/Android Studio.app"
                if os.path.exists(app):
                    utils.execute_shell('cp -R "{app}" /Applications'.format(app=app))
                    utils.execute_shell('hdiutil detach -quiet {dir}'.format(dir=app_dir))
                    console.success('Android Studio安装成功')
                    return
        console.error('Android Studio安装失败')


def _get_download_url(url, pattern_str):
    response = requests.get(url)
    content = response.content.decode('utf-8')
    pattern = re.compile(pattern_str)
    result = pattern.search(content) if pattern else None
    download_url = result.group(1) if result else ''
    return download_url


def _pod():
    if utils.command_exists('pod'):
        console.tips('已安装Pod')
        return True

    if utils.execute_shell('brew install cocoapods'):
        if utils.command_exists('pod'):
            console.success('Pod安装成功')
            return True

    console.error('Pod安装失败')
    return False


def _java():
    # if utils.command_exists('java'):
    #     console.tips('已安装Java')
    #     return True

    if utils.execute_shell('brew tap caskroom/versions') and utils.execute_shell('brew cask install java8'):
        if utils.command_exists('java'):
            console.success('Java安装成功')
            return True

    console.error('Java安装失败')
    return False


def _gradle(shell_config):
    if utils.command_exists('gradle'):
        console.tips('已安装Gradle')
        return True
    gradle_home = os.environ.get('GRADLE_HOME') if os.environ.get('GRADLE_HOME') else ''
    is_download = _download_file(url='https://services.gradle.org/distributions/gradle-3.3-all.zip',
                                 dst=GRADLE_ZIP,
                                 tips='downloading Gradle-3.3')
    if is_download:

        # shutil.unpack_archive(GRADLE_ZIP, GRADLE_DIR)
        zip = zipfile.ZipFile(GRADLE_ZIP)
        zip.extractall(GRADLE_DIR)
        if not os.environ.get('GRADLE_HOME'):
            insert_gradle_home = r"sed -i '' '/^export PATH/i \
            export GRADLE_HOME={gradle_file} \
            ' {shell_config}"
            insert_path = r"sed -i '' 's/^\(export PATH=\)\(.*\)/\1\2:$GRADLE_HOME\/bin/' {shell_config}"
            utils.execute_shell(insert_gradle_home.format(gradle_file=GRADLE, shell_config=shell_config))
            utils.execute_shell(insert_path.format(shell_config=shell_config))
        elif (not gradle_home) or (gradle_home not in os.environ.get('PATH')):
            insert_path = r"sed -i '' 's/^\(export PATH=\)\(.*\)/\1\2:$GRADLE_HOME\/bin/' {shell_config}"
            utils.execute_shell(insert_path.format(shell_config=shell_config))
        GRADLE_BIN = GRADLE+'/bin'
        utils.execute_shell('chmod 777 {GRADLE_BIN}'.format(GRADLE_BIN=GRADLE_BIN))

        # 如果~/.gradle文件夹不存在，则创建文件夹
        if not os.path.exists(os.path.expanduser('~/.gradle')):
            utils.execute_shell('mkidr ~/.gradle')

        # 如果gradle.zip下载成功，则将其移到./gradle文件夹中
        if os.path.exists(GRADLE_ZIP):
            utils.execute_shell('mv {GRADLE_ZIP} ~/.gradle'.format(GRADLE_ZIP=GRADLE_ZIP))

        console.success('Gradle安装成功')
        return True

    console.error('Gradle安装失败')
    return False


def _n():
    if utils.command_exists('n'):
        return True

    if utils.command_exists('npm'):
        utils.execute_shell('npm install -g n')
        return True

    install_shell = 'curl -L https://git.io/n-install | bash -s -- -q'
    return utils.execute_shell(install_shell)


def _wax(shell_config):
    if utils.command_exists('wax'):
        console.tips('已安装Wax')
        return True

    if _node(shell_config):
        if not utils.command_exists('wnpm'):
            utils.execute_shell('npm install -g wnpm')

        if utils.execute_shell('wnpm i -g @wac/wax-cli'):
            console.success('wax安装成功')
            return True

    console.error('Wax安装失败')
    return False


def _xcode():
    if os.path.exists('/Applications/Xcode.app'):
        console.tips('已安装Xcode')
        return True

    choice = click.prompt('是否下载Xcode？', default='y')
    if choice.lower() == 'y':
        if not utils.command_exists('xcversion'):
            utils.execute_shell('sudo gem install xcode-install')

        if utils.execute_shell('xcversion install 9.4.1'):
            console.success('Xcode安装成功')
            return True
        else:
            console.error('Xcode安装失败')
            return False


def _watchman():
    if utils.command_exists('watchman'):
        return True
    utils.execute_shell('brew install watchman')
    return utils.command_exists('watchman')


def env_install(env_type):
    shell_config = utils.get_shell_config()

    _check_shell_config(shell_config)

    _brew()

    if env_type == 'android' or env_type == 'all':
        _java()
        _android(shell_config)

    if env_type == 'ios' or env_type == 'all':
        _pod()

    if env_type == 'wax' or env_type == 'all':
        _wax(shell_config)
        _watchman()

    if env_type == 'android_studio' or env_type == 'all':
        _android_studio()

    if env_type == 'xcode' or env_type == 'all':
        _xcode()


def _check_shell_config(shell_config):
    if shell_config and not os.path.exists(shell_config):
        try:
            file = open(shell_config, 'w')
            file.write('PATH=$PATH')
            file.close()
        except:
            pass

    result = utils.get_shell_result("sed -n '/^export PATH=/p' {shell_config}".format(shell_config=shell_config))
    if not result:
        try:
            file = open(shell_config, 'a')
            file.write('export PATH=$PATH')
            file.close()
        except:
            pass
