import json


result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""


file1 = json.load(open('tests/fixtures/file1.json'))
file2 = json.load(open('tests/fixtures/file2.json'))
