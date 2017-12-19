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


def test_gy_show():
    assert execute(['gy', 'show'])


def test_gy_generate():
    assert execute(['gy', 'generate'])


def test_gy_help():
    assert execute(['gy', '--help'])
