from collections import namedtuple

Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

result_list = [
    Diff_str('-', 'follow', False),
    Diff_str(' ', 'host', 'hexlet.io'),
    Diff_str('-', 'proxy', '123.234.53.22'),
    Diff_str('-', 'timeout', 50),
    Diff_str('+', 'timeout', 20),
    Diff_str('+', 'verbose', True)
]

result_string = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
