========
Overview
========



A simple wrapper around fs to work with flask and switch between local and s3fs

* Free software: MIT license

Installation
============

::

    pip install efs

Documentation
=============

https://python-efs.readthedocs.io/

Development
===========

To run the all tests run::

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


Changelog
=========

0.2.0 (2018-08-22)
------------------

* Upgrade fs to version 2 `#4 <https://github.com/eatfirst/python-efs/pull/4>`_.


0.1.1 (2017-10-16)
------------------

* Add get_filesystem to efs root's package `#2 <https://github.com/eatfirst/python-efs/pull/2>`_.


0.1.0 (2017-10-13)
------------------

* First release on PyPI.


