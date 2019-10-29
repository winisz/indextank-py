#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'indextank',
    version = '1.0.6',
    description = 'IndexTank API Client for Python',
    packages = find_packages(),
    install_requires = ["anyjson"],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
