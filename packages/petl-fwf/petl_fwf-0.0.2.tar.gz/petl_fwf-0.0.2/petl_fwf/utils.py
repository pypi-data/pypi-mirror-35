#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT copyright
from __future__ import ( 
    absolute_import, division, generators, nested_scopes,
    print_function, unicode_literals, with_statement)
from builtins import (
    object, range, str, chr, hex, input, next, oct, open,
    pow, round, super, filter, map, zip)
import itertools
import operator
import six
PY2 = six.PY2
PY3 = six.PY3
TEXT_TYPE = six.text_type
STRING_TYPES = six.string_types

try:
    from itertools import accumulate
except ImportError:
    def accumulate(iterable, func=operator.add):
        """Back-ported version of accumulate"""
        # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
        # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
        it = iter(iterable)
        try:
            total = next(it)
        except StopIteration:
            return
        yield total
        for element in it:
            total = func(total, element)
            yield total

try:
    from itertools import zip_longest as izip_longest  
except ImportError:
    from itertools import izip_longest  # For Python 2


def _ensure_unicode(text):
    r"""
    Casts bytes into utf8 (mostly for python2 compatibility)
    From Erotemic's ubelt: https://github.com/Erotemic/ubelt/blob/master/ubelt
    """
    if text is None:
        return None
    if isinstance(text, six.text_type):
        return text
    if isinstance(text, six.binary_type):
        return text.decode('utf8')
    err_message = 'The provided value was not a text or bytes value!'
    if text: # Not an empty object
        err_message += '\nProvided value:{!r}'.format(text)
    raise ValueError(err_message)
