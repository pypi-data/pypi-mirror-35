#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT copyright
from __future__ import (print_function, unicode_literals)
from builtins import str
"""petl_extras packaging information"""

changelog = {
    '0.0.1': [
        'Initial Release'
    ],
    '0.0.2': [
        'Removed C parser to simplify code',
        'Added tests',
        'Fixed bug that would not read header from a file if a header was not provided'
    ]
}

__version__ = '0.0.2'

license = 'MIT'
description = 'Additional methods for the petl library that enable reading fixed-width files'
author = 'Joseph T. Bradley'
author_email = 'jtbradley@gmail.com'

classifiers = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3'
              ]

long_desc = """
Provides 2 additional methods that work with the petl package.
    fromfwf:    Reads a Fixed-width file (fwf)
    skiplast:   Like petl.skip, except it will skip the last n rows of a Table
"""
