#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT copyright
from __future__ import ( 
    absolute_import, division, generators, nested_scopes,
    print_function, unicode_literals, with_statement)
from builtins import (
    object, range, str, chr, hex, input, next, oct, open,
    pow, round, super, filter, map, zip)
import collections
import itertools
try:
    from petl import Table
except ImportError:
    print('You must install petl to use this package.')

__all__ = ['skiplast']

def skiplast(table, row_count):
    """
    Return all but the last `row_count` rows. E.g.::

        >>> import petl as etl
        >>> table1 = [['foo', 'bar'],
        ...           ['a', 1],
        ...           ['b', 2],
        ...           ['c', 3],
        ...           ['FOOTER ROW']]
        >>> table2 = etl.skiplast(table1, 1)
        >>> table2
        +-----+-----+
        | foo | bar |
        +=====+=====+
        | 'a' |   1 |
        +-----+-----+
        | 'b' |   2 |
        +-----+-----+
        | 'c' |   3 |
        +-----+-----+

    This can be combined with skip to skip the header and footer of a source:
        >>> table1 = [['HEADER ROW'],
        ...           ['foo', 'bar'],
        ...           ['a', 1],
        ...           ['b', 2],
        ...           ['c', 3],
        ...           ['FOOTER ROW']]
        >>> table2 = etl.skiplast(etl.skip(table1, 1), 1)
        >>> table2
        +-----+-----+
        | foo | bar |
        +=====+=====+
        | 'a' |   1 |
        +-----+-----+
        | 'b' |   2 |
        +-----+-----+
        | 'c' |   3 |
        +-----+-----+
    """
    return SkipLastView(table, skiprows=row_count)


class SkipLastView(Table):

    def __init__(self, source, skiprows):
        self.source = source
        self.skiprows = skiprows

    def __iter__(self):
        return iterskiplast(self.source, self.skiprows)


def iterskiplast(table, row_count=None):
    """
    Skips the last row_count rows of the provided table
    """
    it = iter(table)
    hdr = next(it)
    yield hdr
    last_n_elems = collections.deque(itertools.islice(it, row_count), row_count)
    for elem in it:
        yield last_n_elems.popleft()
        last_n_elems.append(elem)
