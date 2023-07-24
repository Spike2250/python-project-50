from collections import namedtuple

Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

simple = [
    Diff_str('-', 'follow', False),
    Diff_str(' ', 'host', 'hexlet.io'),
    Diff_str('-', 'proxy', '123.234.53.22'),
    Diff_str('-', 'timeout', 50),
    Diff_str('+', 'timeout', 20),
    Diff_str('+', 'verbose', True)
]

nest = [
    Diff_str('-', 'follow', False),
    Diff_str('+', 'follow', True),
    Diff_str(' ', 'host', 'hexlet.io'),
    Diff_str(' ', 'proxy', '123.234.53.22'),
    Diff_str(' ', 'setting1', [
        Diff_str('-', 'key1', 44),
        Diff_str('+', 'key1', None),
        Diff_str(' ', 'key2', True),
        Diff_str(' ', 'key3', [
            Diff_str('-', 'aaa', 42),
            Diff_str('+', 'xxx', 42)])]),
    Diff_str(' ', 'timeout', 50)
]

difficult = [
    Diff_str(' ', 'common', [
        Diff_str('+', 'follow', False),
        Diff_str(' ', 'setting1', 'Value 1'),
        Diff_str('-', 'setting2', 200),
        Diff_str('-', 'setting3', True),
        Diff_str('+', 'setting3', None),
        Diff_str('+', 'setting4', 'blah blah'),
        Diff_str('+', 'setting5', [
            Diff_str(' ', 'key5', 'value5')]),
        Diff_str(' ', 'setting6', [
            Diff_str(' ', 'doge', [
                Diff_str('-', 'wow', ''),
                Diff_str('+', 'wow', 'so much')]),
            Diff_str(' ', 'key', 'value'),
            Diff_str('+', 'ops', 'vops')])
    ]),
    Diff_str(' ', 'group1', [
        Diff_str('-', 'baz', 'bas'),
        Diff_str('+', 'baz', 'bars'),
        Diff_str(' ', 'foo', 'bar'),
        Diff_str('-', 'nest', [
            Diff_str(' ', 'key', 'value')]),
        Diff_str('+', 'nest', 'str')
    ]),
    Diff_str('-', 'group2', [
        Diff_str(' ', 'abc', 12345),
        Diff_str(' ', 'deep', [
            Diff_str(' ', 'id', 45)])
    ]),
    Diff_str('+', 'group3', [
        Diff_str(' ', 'deep', [
            Diff_str(' ', 'id', [
                Diff_str(' ', 'number', 45)])]),
        Diff_str(' ', 'fee', 100500)
    ])
]
