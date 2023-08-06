**DO NOT USE THIS LIBRARY**: it was written to support `InteractiveCommandLine <https://github.com/jacquev6/InteractiveCommandLine>`_,
and the `click <http://click.pocoo.org/>`_ library is vastly better.
I will not fix anything in this library and I'm migrating my own projects to ``click``.

RecursiveDocument is a Python (2.7+ and 3.3+) library formating, in a console-friendly and human-readable way,
a document specified through its structure (sections, sub-sections, paragraphs, etc.).
It is especially well suited for printing help messages for command-line executables.

It's licensed under the `MIT license <http://choosealicense.com/licenses/mit/>`__.
It's available on the `Python package index <http://pypi.python.org/pypi/RecursiveDocument>`__,
its `documentation is hosted by Python <http://pythonhosted.org/RecursiveDocument>`__
and its source code is on `GitHub <https://github.com/jacquev6/RecursiveDocument>`__.

.. image:: https://img.shields.io/travis/jacquev6/RecursiveDocument/master.svg
    :target: https://travis-ci.org/jacquev6/RecursiveDocument

.. image:: https://img.shields.io/coveralls/jacquev6/RecursiveDocument/master.svg
    :target: https://coveralls.io/r/jacquev6/RecursiveDocument

.. image:: https://img.shields.io/codeclimate/github/jacquev6/RecursiveDocument.svg
    :target: https://codeclimate.com/github/jacquev6/RecursiveDocument

.. image:: https://img.shields.io/scrutinizer/g/jacquev6/RecursiveDocument.svg
    :target: https://scrutinizer-ci.com/g/jacquev6/RecursiveDocument

.. image:: https://img.shields.io/pypi/dm/RecursiveDocument.svg
    :target: https://pypi.python.org/pypi/RecursiveDocument

.. image:: https://img.shields.io/pypi/l/RecursiveDocument.svg
    :target: https://pypi.python.org/pypi/RecursiveDocument

.. image:: https://img.shields.io/pypi/v/RecursiveDocument.svg
    :target: https://pypi.python.org/pypi/RecursiveDocument

.. image:: https://img.shields.io/pypi/pyversions/RecursiveDocument.svg
    :target: https://pypi.python.org/pypi/RecursiveDocument

.. image:: https://img.shields.io/pypi/status/RecursiveDocument.svg
    :target: https://pypi.python.org/pypi/RecursiveDocument

.. image:: https://img.shields.io/github/issues/jacquev6/RecursiveDocument.svg
    :target: https://github.com/jacquev6/RecursiveDocument/issues

.. image:: https://badge.waffle.io/jacquev6/RecursiveDocument.png?label=ready&title=ready
    :target: https://waffle.io/jacquev6/RecursiveDocument

.. image:: https://img.shields.io/github/forks/jacquev6/RecursiveDocument.svg
    :target: https://github.com/jacquev6/RecursiveDocument/network

.. image:: https://img.shields.io/github/stars/jacquev6/RecursiveDocument.svg
    :target: https://github.com/jacquev6/RecursiveDocument/stargazers

Quick start
===========

Install from PyPI::

    $ pip install RecursiveDocument

Import:

>>> from RecursiveDocument import *

Create a document:

>>> doc = Document().add(
...   Section("Introduction")
...     .add("This is the first paragraph of a very interesting story. It begins with this paragraph.")
...     .add("After the first paragraph comes the second paragraph. As incredible as it may sound, it can go on and on and on...")
... )

And print it:

>>> print doc.format()
Introduction
  This is the first paragraph of a very interesting story. It begins
  with this paragraph.
<BLANKLINE>
  After the first paragraph comes the second paragraph. As incredible
  as it may sound, it can go on and on and on...
