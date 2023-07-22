from collections import namedtuple

Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

result_list_1 = [
    Diff_str('-', 'follow', False),
    Diff_str(' ', 'host', 'hexlet.io'),
    Diff_str('-', 'proxy', '123.234.53.22'),
    Diff_str('-', 'timeout', 50),
    Diff_str('+', 'timeout', 20),
    Diff_str('+', 'verbose', True)
]

result_list_2 = [
    Diff_str(' ', 'common', [
        Diff_str('+', 'follow', False),
        Diff_str(' ', 'settings1', 'Value 1'),
        Diff_str('-', 'settings2', 200),
        Diff_str('-', 'settings3', True),
        Diff_str('+', 'settings3', None),
    ])
]

result_string_1 = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


result_string_2 = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""  # noqa: W291
