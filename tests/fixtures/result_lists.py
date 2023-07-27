from collections import namedtuple

Diff = namedtuple('Diff', ('status', 'key', 'value'))

simple = [
    Diff('-', 'follow', False),
    Diff(' ', 'host', 'hexlet.io'),
    Diff('-', 'proxy', '123.234.53.22'),
    Diff('-', 'timeout', 50),
    Diff('+', 'timeout', 20),
    Diff('+', 'verbose', True)
]

nest = [
    Diff('-', 'follow', False),
    Diff('+', 'follow', True),
    Diff(' ', 'host', 'hexlet.io'),
    Diff(' ', 'proxy', '123.234.53.22'),
    Diff(' ', 'setting1', [
        Diff('-', 'key1', 44),
        Diff('+', 'key1', None),
        Diff(' ', 'key2', True),
        Diff(' ', 'key3', [
            Diff('-', 'aaa', 42),
            Diff('+', 'xxx', 42)])]),
    Diff(' ', 'timeout', 50)
]

difficult = [
    Diff(' ', 'common', [
        Diff('+', 'follow', False),
        Diff(' ', 'setting1', 'Value 1'),
        Diff('-', 'setting2', 200),
        Diff('-', 'setting3', True),
        Diff('+', 'setting3', None),
        Diff('+', 'setting4', 'blah blah'),
        Diff('+', 'setting5', [
            Diff(' ', 'key5', 'value5')]),
        Diff(' ', 'setting6', [
            Diff(' ', 'doge', [
                Diff('-', 'wow', ''),
                Diff('+', 'wow', 'so much')]),
            Diff(' ', 'key', 'value'),
            Diff('+', 'ops', 'vops')])
    ]),
    Diff(' ', 'group1', [
        Diff('-', 'baz', 'bas'),
        Diff('+', 'baz', 'bars'),
        Diff(' ', 'foo', 'bar'),
        Diff('-', 'nest', [
            Diff(' ', 'key', 'value')]),
        Diff('+', 'nest', 'str')
    ]),
    Diff('-', 'group2', [
        Diff(' ', 'abc', 12345),
        Diff(' ', 'deep', [
            Diff(' ', 'id', 45)])
    ]),
    Diff('+', 'group3', [
        Diff(' ', 'deep', [
            Diff(' ', 'id', [
                Diff(' ', 'number', 45)])]),
        Diff(' ', 'fee', 100500)
    ])
]
