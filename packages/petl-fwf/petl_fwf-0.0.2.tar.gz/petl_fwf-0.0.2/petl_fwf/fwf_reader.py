#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT copyright
from __future__ import ( 
    absolute_import, division, generators, nested_scopes,
    print_function, unicode_literals, with_statement)
from builtins import (
    object, range, str, chr, hex, input, next, oct, open,
    pow, round, super, filter, map, zip)
import io


try:
    from petl import (fromtext, Table, skip)
    from petl.io.base import getcodec
    from petl.io.sources import read_source_from_arg
except ImportError:
    print('You must install petl to use this package.')
    raise

from .utils import (
    PY2, PY3,
    TEXT_TYPE, STRING_TYPES,
    accumulate, izip_longest,
    _ensure_unicode)
from .skiplast import skiplast

__all__ = ['fromfwf']


def _get_fw_parser(widths):
    """
    Returns a function that will split a fixed-width string.
    """
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in widths))
    pads = tuple(fw < 0 for fw in widths) # bool values for padding fields
    flds = tuple(izip_longest(pads, (0,) + cuts, cuts))[:-1]  # ignore final one
    parser = lambda line: tuple(line[i:j] for pad, i, j in flds if not pad)
    return parser


def fromfwf(source=None, widths=None, encoding=None, errors='strict',
            header=None, skiprows=None, skipfooter=None):
    """
    Extract a table (As defined by the petl package) from lines in the given fixed-width file.

        >>> import fromfwf
        >>> # setup a sample file
        ... text = '  18 5 2\\n2018 5 2\\n20180502'
        >>> with open('example.txt', 'w') as f:
        ...    f.write(text)
        ...
        28
        >>> table1 = etl.fromfwf('example.txt', widths=[4, 2, 2])
        >>> table1
        +--------+------+------+
        | lines  |      |      |
        +========+======+======+
        | '  18' | ' 5' | ' 2' |
        +--------+------+------+
        | '2018' | ' 5' | ' 2' |
        +--------+------+------+
        | '2018' | '05' | '02' |
        +--------+------+------+
        >>> # Specify headers for the file
        ... table1 = etl.fromfwf('example.txt', widths=[4, 2, 2], header=['year', 'month', 'day'])
        >>> table1
        +--------+-------+------+
        | year   | month | day  |
        +========+=======+======+
        | '  18' | ' 5'  | ' 2' |
        +--------+-------+------+
        | '2018' | ' 5'  | ' 2' |
        +--------+-------+------+
        | '2018' | '05'  | '02' |
        +--------+-------+------+
    """
    if widths is None:
        raise AttributeError('No field widths provided!')
    if isinstance(widths, (list, tuple)) is False:
        raise AttributeError('Field widths must be a tuple or list of field widths!')
    if isinstance(source, Table):
        source = source
    else:
        source = read_source_from_arg(source)
    return FixedTextView(source, widths=widths, header=header, encoding=encoding,
                         errors=errors, skiprows=skiprows, skipfooter=skipfooter)


class FixedTextView(Table):

    def __init__(self, source=None, widths=None, header=None, encoding=None,
                 errors=None, skiprows=None, skipfooter=None):
        self.source = source
        self.widths = widths
        self.skiprows = skiprows
        self.skipfooter = skipfooter
        self._rowparser = _get_fw_parser(widths)
        self.header = None
        if header:
            if isinstance(header, (list, tuple)):
                self.header = tuple(header)
            elif isinstance(header, STRING_TYPES):
                self.header = tuple(self._rowparser(header))
        self.encoding = encoding or 'utf-8'
        self.errors = errors or 'strict'


    def __iter__(self):
        with self.source.open('rb') as buf:
            if PY2:
                codec = getcodec(self.encoding)
                fr = codec.streamreader(buf, errors=self.errors)
            else:
                fr = io.TextIOWrapper(buf,
                                      encoding=self.encoding,
                                      errors=self.errors,
                                      newline='')
            # Skip headers and footers before trying to parse rows
            f = iter(fr)
            if self.skiprows:
                f = skip(f, self.skiprows)
            if self.skipfooter:
                f = skiplast(f, self.skipfooter)
            try:
                if self.header is not None:
                    yield tuple(self.header)
                for raw_line in f:
                    yield self._rowparser(raw_line)
            finally:
                if not PY2:
                    fr.detach()
