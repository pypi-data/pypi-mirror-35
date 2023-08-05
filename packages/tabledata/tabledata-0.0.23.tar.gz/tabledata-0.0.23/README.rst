tabledata
===========
.. image:: https://badge.fury.io/py/tabledata.svg
    :target: https://badge.fury.io/py/tabledata

.. image:: https://img.shields.io/pypi/pyversions/tabledata.svg
   :target: https://pypi.python.org/pypi/tabledata

.. image:: https://img.shields.io/travis/thombashi/tabledata/master.svg?label=Linux/macOS
    :target: https://travis-ci.org/thombashi/tabledata
    :alt: Linux CI test status

.. image:: https://img.shields.io/appveyor/ci/thombashi/tabledata/master.svg?label=Windows
    :target: https://ci.appveyor.com/project/thombashi/tabledata/branch/master
    :alt: Windows CI test status

.. image:: https://coveralls.io/repos/github/thombashi/tabledata/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/tabledata?branch=master

Summary
---------
A Python library to represent tabular data for pytablewriter/pytablereader/SimpleSQLite.

Installation
============
::

    pip install tabledata


Dependencies
============
Python 2.7+ or 3.4+

Mandatory Python packages
----------------------------------
- `DataPropery <https://github.com/thombashi/DataProperty>`__ (Used to extract data types)
- `logbook <http://logbook.readthedocs.io/en/stable/>`__
- `pathvalidate <https://github.com/thombashi/pathvalidate>`__
- `six <https://pypi.python.org/pypi/six/>`__
- `typepy <https://github.com/thombashi/typepy>`__

Optional Python packages
------------------------------------------------
- `pandas <http://pandas.pydata.org/>`__
    - required to get table data as a pandas data frame

Test dependencies
-----------------
- `pytablewriter <https://github.com/thombashi/pytablewriter>`__
- `pytest <http://pytest.org/latest/>`__
- `pytest-runner <https://pypi.python.org/pypi/pytest-runner>`__
- `tox <https://testrun.org/tox/latest/>`__

Documentation
===============
https://tabledata.rtfd.io/

