# coding: utf8

"""
    gy generates .gitignore files from the command line for you.
"""

import click


@click.group()
def cli():
    """Yet another .gitignore magician in your command line."""
    pass


@cli.command()
def update():
    """update .gitignore zip"""
    click.echo('update .gitignore zip')


@cli.command()
def show():
    """show all supported languages"""
    click.echo('show all supported languages')


@cli.command()
@click.argument('language', required=False)
def generate(language):
    """generate .gitignore file"""
    language = 'Python' or language
    click.echo('generate .gitignore file for {0}'.format(language))


def main():
    """
    :return:
    """
    cli()


if __name__ == '__main__':
    main()
