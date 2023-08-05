#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py: Setup information.
# Copyright (C) 2010 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright (C) 2018 Nuxeo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
from setuptools import setup

PKG_DIR = "pathtools"

try:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "version", os.path.join(PKG_DIR, "version.py")
    )
    version = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(version)
except ImportError:
    import imp

    version = imp.load_source("version", os.path.join(PKG_DIR, "version.py"))


def read_file(filename):
    """
    Reads the contents of a given file relative to the directory
    containing this file and returns it.

    :param filename:
        The file to open and read contents from.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name="pathtools3",
    version=version.VERSION_STRING,
    description="File system general utilities",
    long_description=read_file("README.rst"),
    author="Nuxeo",
    author_email="maintainers-python@nuxeo.com",
    license="MIT License",
    url="https://github.com/nuxeo/pathtools3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    packages=["pathtools"],
)
