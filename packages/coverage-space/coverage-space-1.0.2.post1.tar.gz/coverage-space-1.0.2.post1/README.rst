Unix: |Unix Build Status| Windows: |Windows Build Status|\ Metrics:
|Coverage Status| |Scrutinizer Code Quality|\ Usage: |PyPI Version|

Overview
========

The official command-line client for `The Coverage
Space <http://coverage.space>`__.

Setup
=====

Requirements
------------

-  Python 2.7+ or Python 3.3+

Installation
------------

The client can be installed with pip:

.. code:: sh

    $ pip install --upgrade coverage-space

or directly from the source code:

.. code:: sh

    $ git clone https://github.com/jacebrowning/coverage-space-cli.git
    $ cd coverage-space-cli
    $ python setup.py install

Usage
=====

To update the value for a test coverage metric:

.. code:: sh

    $ coverage.space <owner/repo> <metric>

For example, after testing with code coverage enabled:

.. code:: sh

    $ coverage.space owner/repo unit

will attempt to extract the current coverage data from your working tree
and compare that with the last known value. The coverage value can also
be manually specified:

.. code:: sh

    $ coverage.space <owner/repo> <metric> <value>

.. |Unix Build Status| image:: http://img.shields.io/travis/jacebrowning/coverage-space-cli/develop.svg
   :target: https://travis-ci.org/jacebrowning/coverage-space-cli
.. |Windows Build Status| image:: https://img.shields.io/appveyor/ci/jacebrowning/coverage-space-cli/develop.svg
   :target: https://ci.appveyor.com/project/jacebrowning/coverage-space-cli
.. |Coverage Status| image:: http://img.shields.io/coveralls/jacebrowning/coverage-space-cli/develop.svg
   :target: https://coveralls.io/r/jacebrowning/coverage-space-cli
.. |Scrutinizer Code Quality| image:: http://img.shields.io/scrutinizer/g/jacebrowning/coverage-space-cli.svg
   :target: https://scrutinizer-ci.com/g/jacebrowning/coverage-space-cli/?branch=develop
.. |PyPI Version| image:: http://img.shields.io/pypi/v/coverage.space.svg
   :target: https://pypi.python.org/pypi/coverage.space
