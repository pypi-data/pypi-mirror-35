pathtools
=========

Pattern matching and various utilities for file systems paths.


Installing
----------

As simple as:

    python3 -m pip install --upgrade --user pathtools3

Or from sources:

    python3 -m pip install -e .


Testing
-------

Requirements:

    python3 -m pip install pytest pytest-cov

And then:

    python3 -m pytest


Deploying
---------

For the maintainer, you will need to install wheel:

    python3 -m pip install wheel

And the command to distribute the module is:

    python3 setup.py sdist bdist_wheel upload
