# coding: utf8

"""
    gy generates .gitignore files from the command line for you.
"""

import os
import shutil
import zipfile

import click
import requests

HERE = os.path.abspath(os.path.dirname(__file__))
IGNORE_ZIP_URL = 'https://codeload.github.com/github/gitignore/zip/master'
IGNORE_ZIP_NAME = 'ignore-master.zip'
ARCHIVE_DIR = 'archive'
SUFFIX = '.gitignore'


def _unzip(archive, target):
    """
    :param archive:
    :param target:
    :return:
    """
    with zipfile.ZipFile(archive, 'r') as z:
        z.extractall(target)


def _download_zip(url):
    """
    :param url:
    :return:
    """
    r = requests.get(url)
    if r.status_code == 200:
        parent = os.path.join(HERE, ARCHIVE_DIR)
        if not os.path.exists(parent):
            os.mkdir(parent)
        path = os.path.join(parent, IGNORE_ZIP_NAME)
        with open(path, 'w') as f:
            f.write(r.content)
        _unzip(path, parent)
        os.remove(path)


def _remove_files(target):
    """
    :param target:
    :return:
    """
    path = os.path.join(HERE, target)
    if os.path.exists(path):
        shutil.rmtree(path)


def wrap_files():
    """
    :return:
    """
    gd = dict()
    path = os.path.join(HERE, ARCHIVE_DIR)
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(SUFFIX):
                gd[f.replace(SUFFIX, '', 1).lower()] = os.path.join(root, f)

    return gd


def ls_ignores():
    """
    :return:
    """
    return [k for k in wrap_files()]


def ge_ignores(names):
    """
    :param names:
    :return:
    """
    ignores_map = wrap_files()
    if not ignores_map:
        click.secho(click.style('archive folder is empty, please run `gy update` first.', fg='red'))
        return
    unknown_list = list()
    output_list = list()
    for l in names:
        if l.lower() not in ignores_map:
            unknown_list.append(l)
        else:
            with open(ignores_map[l.lower()], 'r') as f:
                hint = '--- {0} begin ---\n{1}---- {2} end ----\n'.format(l, f.read(), l)
                output_list.append(hint)

    click.echo('\n'.join(output_list))
    if unknown_list:
        click.secho(click.style('unsupported files: {0}'.format(', '.join(unknown_list)), fg='yellow'))
        click.secho(click.style('run `gy ls` to see all supported languages.'), fg='yellow')


@click.group()
def cli():
    """Yet another .gitignore magician in your command line."""
    pass


@cli.command()
def update():
    """update archive folder"""
    tasks = [('_remove_files', 'ARCHIVE_DIR'), ('_download_zip', 'IGNORE_ZIP_URL')]
    with click.progressbar(tasks, label='updating archive folder') as bar:
        for t in bar:
            exec ('{0}({1})'.format(t[0], t[1]))


@cli.command()
def ls():
    """list all supported languages"""
    ignores_list = ls_ignores()
    if not ignores_list:
        click.secho(click.style('archive folder is empty, please run `gy update` first.', fg='red'))
        return
    click.secho(click.style('{0} supported .gitignore files:'.format(len(ignores_list)), fg='blue'))
    ignores_list.sort()
    click.secho(click.style(', '.join(ignores_list), fg='green'))


@cli.command()
@click.argument('languages', nargs=-1)
def generate(languages):
    """generate .gitignore file"""
    ge_ignores(languages)


if __name__ == '__main__':
    cli()
