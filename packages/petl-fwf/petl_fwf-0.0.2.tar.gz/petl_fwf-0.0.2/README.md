# petl_fwf
This package contains two additional methods which add the ability to read fixed-width files to the fabulous [petl package](https://github.com/petl-developers/petl). 

## fromfwf
This is the primary method which this package adds. Usage is straightforward, and similar to other methods in the petl library

```sh
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
```

## skiplast
This method will skip the last n rows of a table.
```sh
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
```
