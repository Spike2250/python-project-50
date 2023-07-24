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
