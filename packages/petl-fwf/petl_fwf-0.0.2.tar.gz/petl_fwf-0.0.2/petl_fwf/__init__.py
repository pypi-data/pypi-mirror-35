#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT copyright
from __future__ import ( 
    absolute_import, print_function, unicode_literals)
from builtins import (
    object, range, str, chr, hex, input, next, oct, open,
    pow, round, super, filter, map, zip)
__doc__ = """
Provides additional methods for petl that allow it to read fixed-width files
    fromfwf:    Reads a Fixed-width file (fwf)
    skiplast:   Like petl.skip, except it will skip the last n rows of a Table
"""
from .fwf_reader import fromfwf
from .skiplast import skiplast
__all__ = ['fromfwf', 'skiplast']
