`diffdirs`: FITS regression testing made easy
=============================================

`diffdirs` is a simple tool to diff two directories containing FITS files. The most obvious use case here is for regression testing of software that produces FITS files. You want to ensure that:

1. The directory structure is identical, except for log files, etc. This includes:

     a) Files in "new" directories that are not in the "original" (i.e. missing files)
     b) Files in the "old" directory that are not in one or more "new" directories (i.e. extra files)
2. The contents of all FITS files are identical, except for certain types of metadata

Installation
------------

Install from pip (recommended):

::

    $ pip install diffdirs

Or, install straight from the repo:

::

    $ git clone https://github.com/GreenBankObservatory/diffdirs
    $ pip install diffdirs

Usage
-----

Use the wrapper script (recommended):

::

    $ diffdirs -h

Call the module:

::

    $ python -m diffdirs -h

Import as library:

::

    $ python
    >>> from diffdirs.diffdirs import diff_dirs
    >>> help(diff_dirs)

Build
-----

To build bundles for publication:

::

    $ rm -rf dist/* && python setup.py sdist && python setup.py bdist_wheel

Publish
-------

::

    $ twine upload dist/*
