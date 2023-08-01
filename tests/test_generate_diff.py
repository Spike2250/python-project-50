import pytest
import json
import yaml
from pathlib import Path
from tests.fixtures import result_lists as lists
from tests.fixtures import result_stylish_strings
from tests.fixtures import result_plain_strings

from gendiff.diff import analyse_diff_files
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain


@pytest.fixture
def coll():
    path = 'tests/fixtures/'
    path_file1_simple_json = Path(Path.cwd(), path, 'file1_simple.json')
    path_file2_simple_json = Path(Path.cwd(), path, 'file2_simple.json')
    path_file1_nest_json = Path(Path.cwd(), path, 'file1_nest.json')
    path_file2_nest_json = Path(Path.cwd(), path, 'file2_nest.json')
    path_file1_json = Path(Path.cwd(), path, 'file1.json')
    path_file2_json = Path(Path.cwd(), path, 'file2.json')
    path_file1_simple_yml = Path(Path.cwd(), path, 'file1_simple.yaml')
    path_file2_simple_yml = Path(Path.cwd(), path, 'file2_simple.yaml')
    path_file1_nest_yml = Path(Path.cwd(), path, 'file1_nest.yaml')
    path_file2_nest_yml = Path(Path.cwd(), path, 'file2_nest.yaml')
    path_file1_yml = Path(Path.cwd(), path, 'file1.yaml')
    path_file2_yml = Path(Path.cwd(), path, 'file2.yaml')

    return {
        'file1_simple_json': json.load(open(path_file1_simple_json)),
        'file2_simple_json': json.load(open(path_file2_simple_json)),
        'file1_nest_json': json.load(open(path_file1_nest_json)),
        'file2_nest_json': json.load(open(path_file2_nest_json)),
        'file1_json': json.load(open(path_file1_json)),
        'file2_json': json.load(open(path_file2_json)),
        'file1_simple_yml': yaml.safe_load(open(path_file1_simple_yml)),
        'file2_simple_yml': yaml.safe_load(open(path_file2_simple_yml)),
        'file1_nest_yml': yaml.safe_load(open(path_file1_nest_yml)),
        'file2_nest_yml': yaml.safe_load(open(path_file2_nest_yml)),
        'file1_yml': yaml.safe_load(open(path_file1_yml)),
        'file2_yml': yaml.safe_load(open(path_file2_yml)),
    }


@pytest.mark.parametrize('key1, key2, expected', [
    ('file1_simple_json', 'file2_simple_json', lists.simple),
    ('file1_simple_yml', 'file2_simple_yml', lists.simple),
    ('file1_nest_json', 'file2_nest_json', lists.nest),
    ('file1_nest_yml', 'file2_nest_yml', lists.nest),
    ('file1_json', 'file2_json', lists.difficult),
    ('file1_yml', 'file2_yml', lists.difficult)])
def test_analyse_files(coll, key1, key2, expected):
    assert analyse_diff_files(coll[key1], coll[key2]) == expected


@pytest.mark.parametrize('key1, key2, expected1, expected2', [
    ('file1_simple_json', 'file2_simple_json',
        result_stylish_strings.simple, result_plain_strings.simple),
    ('file1_simple_yml', 'file2_simple_yml',
        result_stylish_strings.simple, result_plain_strings.simple),
    ('file1_nest_json', 'file2_nest_json',
        result_stylish_strings.nest, result_plain_strings.nest),
    ('file1_nest_yml', 'file2_nest_yml',
        result_stylish_strings.nest, result_plain_strings.nest),
    ('file1_json', 'file2_json',
        result_stylish_strings.difficult, result_plain_strings.difficult),
    ('file1_yml', 'file2_yml',
        result_stylish_strings.difficult, result_plain_strings.difficult)])
def test_gendiff(coll, key1, key2, expected1, expected2):
    result_s = format_stylish(analyse_diff_files(coll[key1], coll[key2]))
    result_p = format_plain(analyse_diff_files(coll[key1], coll[key2]))
    assert result_s == expected1
    assert result_p == expected2
