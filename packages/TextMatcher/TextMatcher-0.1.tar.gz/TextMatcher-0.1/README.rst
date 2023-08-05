

.. TextMatcher documentation master file, created by startproject.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TextMatcher's documentation!
=================================================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/python-textmatcher
:Keywords: ``textmatcher``
:PythonVersion: 3.6

|build-status| |coverage|

|python-versions| |pypi-version|

Extract data from an web-page or PDF-document and match it with the given text parameter

.. contents::

.. section-numbering::

Installation
============

Requirements
------------

* Python 3.6 or above
* setuptools 30.3.0 or above


Install
-------

.. code-block:: bash

    pip install textmatcher


Usage
=====

.. code-block:: python

    from textmatcher import match

    find = 'Python enabled us to create EVE Online, a massive multiplayer game, in record time.'
    ratio = match('https://www.python.org/about/quotes/', find)

    print(ratio)



.. |build-status| image:: https://travis-ci.org/maykinmedia/python-textmatcher.svg?branch=master
    :target: https://travis-ci.org/maykinmedia/python-textmatcher/

.. |coverage| image:: https://codecov.io/gh/maykinmedia/python-textmatcher/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/python-textmatcher
    :alt: Coverage status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/textmatcher.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/textmatcher.svg
    :target: https://pypi.org/project/textmatcher/
