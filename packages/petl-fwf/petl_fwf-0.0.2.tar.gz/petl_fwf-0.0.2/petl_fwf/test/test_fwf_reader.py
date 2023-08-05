# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division


from tempfile import NamedTemporaryFile
import gzip
import bz2
import os
import io


from petl.test.helpers import ieq, eq_
from petl_fwf.fwf_reader import fromfwf

def test_fromfwf_no_header():
    f = NamedTemporaryFile(delete=False, mode='wb')
    f.write(b'Header text that should not be returned in results\n')
    f.write(b'  a  1\n')
    f.write(b'b  2  \n')
    f.write(b'c  3  \n')
    f.write(b'Footer text that should not be returned in results\n')
    f.close()
    actual = fromfwf(f.name, encoding='ascii', widths=[3, 3], header=('col1', 'col2'),
                     skiprows=1, skipfooter=1)
    expect = (('col1', 'col2'),
              ('  a', '  1'),
              ('b  ', '2  '),
              ('c  ', '3  '))
    ieq(expect, actual)
    ieq(expect, actual)  # verify can iterate twice

def test_fromfwf_with_header():
    f = NamedTemporaryFile(delete=False, mode='wb')
    f.write(b'c1  c2\n')
    f.write(b'  a  1\n')
    f.write(b'b  2  \n')
    f.write(b'c  3  \n')
    f.write(b'Footer text that should not be returned in results\n')
    f.close()
    actual = fromfwf(f.name, encoding='ascii', widths=[3, 3], skipfooter=1)
    expect = (('c1 ', ' c2'),
              ('  a', '  1'),
              ('b  ', '2  '),
              ('c  ', '3  '))
    ieq(expect, actual)
    ieq(expect, actual)  # verify can iterate twice

def test_test_fromfwf_gz_no_header():
    # initial data
    f = NamedTemporaryFile(delete=False)
    f.close()
    fn = f.name + '.gz'
    os.rename(f.name, fn)
    f = gzip.open(fn, 'wb')
    try:
        f.write(b'Header text that should not be returned in results\n')
        f.write(b'  a  1\n')
        f.write(b'b  2  \n')
        f.write(b'c  3  \n')
        f.write(b'Footer text that should not be returned in results\n')
    finally:
        f.close()
    expect = (('col1', 'col2'),
              ('  a', '  1'),
              ('b  ', '2  '),
              ('c  ', '3  '))
    actual = fromfwf(f.name, encoding='ascii', widths=[3, 3], header=('col1', 'col2'),
                     skiprows=1, skipfooter=1)
    ieq(expect, actual)
    ieq(expect, actual)  # verify can iterate twice
