========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pyglassdoor/badge/?style=flat
    :target: https://pyglassdoor.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/hamid-vakilzadeh/pyglassdoor/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/hamid-vakilzadeh/pyglassdoor/actions

.. |codecov| image:: https://codecov.io/gh/hamid-vakilzadeh/pyglassdoor/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/hamid-vakilzadeh/pyglassdoor

.. |version| image:: https://img.shields.io/pypi/v/pyglassdoor.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pyglassdoor

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyglassdoor.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pyglassdoor

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyglassdoor.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pyglassdoor

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyglassdoor.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pyglassdoor

.. |commits-since| image:: https://img.shields.io/github/commits-since/hamid-vakilzadeh/pyglassdoor/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/hamid-vakilzadeh/pyglassdoor/compare/v0.0.2...master



.. end-badges

A python API for glassdoor.com

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pyglassdoor

You can also install the in-development version with::

    pip install https://github.com/hamid-vakilzadeh/pyglassdoor/archive/main.zip


Documentation
=============


https://pyglassdoor.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

