gy
==

.. image:: https://img.shields.io/pypi/l/gy.svg
    :target: https://pypi.python.org/pypi/gy

.. image:: https://img.shields.io/pypi/v/gy.svg
    :target: https://pypi.python.org/pypi/gy

.. image:: https://img.shields.io/pypi/pyversions/gy.svg
    :target: https://pypi.python.org/pypi/gy

.. image:: https://travis-ci.org/cls1991/gy.svg?branch=master
    :target: https://travis-ci.org/cls1991/gy

Yet another .gitignore magician in your command line.

☤ Quickstart
------------

Generate .gitignore for certain language, e.g. Lua:

::

    $ gy generate lua

Multiple languages, e.g. Python, Java, Lisp:

::

    $ gy generate python java lisp

To update archive folder, simply run:

::

    $ gy update

List all supported languages:

::

    $ gy ls

☤ Installation
--------------

You can install "gy" via pip from `PyPI <https://pypi.python.org/pypi/gy>`_:

::

    $ pip install gy
	
☤ Usage
-------

::

    $ gy --help
    Usage: gy [OPTIONS] COMMAND [ARGS]...

    Yet another .gitignore magician in your command line.

    Options:
      --help  Show this message and exit.

    Commands:
      generate  generate .gitignore file
      ls        list all supported languages
      update    update archive folder
