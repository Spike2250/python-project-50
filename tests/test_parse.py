import pytest
import requests
from gendiff.parse import parse_file_format, parse_data


def test_parse_file_format():
    assert parse_file_format('some_file.json') == 'json'
    assert parse_file_format('some.fi.le.json') == 'json'
    assert parse_file_format('kjbn/dsjkfn/rrrr.yml') == 'yaml'
    assert parse_file_format('some_ttt.yaml') == 'yaml'
    assert parse_file_format('df.kjfvkjbn/dsjkfn/ssss.rr') == ''


def test_parse_data():
    with open('tests/fixtures/test.yaml') as f:
        assert parse_data(f, 'yaml') == {'b': 1}

        with pytest.raises(ValueError):
            parse_data(f, 'exe')\

    with open('tests/fixtures/test.json') as f:
        assert parse_data(f, 'json') == {"one": 1, "two": 2}

    data = requests.get('https://api.github.com').text
    assert isinstance(parse_data(data, 'json'), dict)
