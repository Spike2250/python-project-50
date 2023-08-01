import pytest
import json

from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import return_original_structure, format_json

from tests.fixtures import result_lists as lists
from tests.fixtures import result_stylish_strings
from tests.fixtures import result_plain_strings


@pytest.mark.parametrize("input_data, expected", [
    (lists.simple, result_stylish_strings.simple),
    (lists.nest, result_stylish_strings.nest),
    (lists.difficult, result_stylish_strings.difficult)])
def test_format_stylish(input_data, expected):
    assert format_stylish(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    (lists.simple, result_plain_strings.simple),
    (lists.nest, result_plain_strings.nest),
    (lists.difficult, result_plain_strings.difficult)])
def test_format_plain(input_data, expected):
    assert format_plain(input_data) == expected


@pytest.mark.parametrize("input_data", [
    lists.simple, lists.nest, lists.difficult])
def test_format_json(input_data):
    assert format_json(input_data) == json.dumps(input_data, indent=2)


# в связи с использованием namedtuple - просто json.loads не дает полного
# возвращения исходной структуры, после форматера format_json,
# т.к. возвращается список не именнованных кортежей
@pytest.mark.parametrize("input_data", [
    lists.simple, lists.nest, lists.difficult])
def test_return_original_structure(input_data):
    assert return_original_structure(format_json(input_data)) == input_data
