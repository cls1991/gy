# coding: utf8


import subprocess


def execute(cmd):
    out = None
    if cmd:
        try:
            out, err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()
        except ValueError:
            pass

    return out


def test_gy():
    assert execute(['gy'])


def test_gy_update():
    assert execute(['gy', 'update'])


def test_gy_ls():
    assert execute(['gy', 'ls'])


def test_gy_generate():
    assert execute(['gy', 'generate'])
    assert execute(['gy', 'generate', 'java'])
    assert execute(['gy', 'generate', 'java', 'lua'])


def test_gy_help():
    assert execute(['gy', '--help'])
