import pytest
import json
import yaml
from pathlib import Path
from tests.fixtures import result_lists as lists
from tests.fixtures import result_stylish_strings
from tests.fixtures import result_plain_strings

from gendiff.diff.analyse import analyse_diff_files
from gendiff.diff.formaters.stylish import format_stylish
from gendiff.diff.formaters.plain import format_plain


@pytest.fixture
def coll():
    path = 'tests/fixtures/'
    # плоские структуры
    file2_simple_json = 'file2_simple.json'
    file1_simple_json = 'file1_simple.json'
    file1_simple_yml = 'file1_simple.yaml'
    file2_simple_yml = 'file2_simple.yaml'
    # вложенные структуры
    file1_nest_json = 'file1_nest.json'
    file2_nest_json = 'file2_nest.json'
    file1_json = 'file1.json'
    file2_json = 'file2.json'
    file1_nest_yml = 'file1_nest.yaml'
    file2_nest_yml = 'file2_nest.yaml'
    file1_yml = 'file1.yaml'
    file2_yml = 'file2.yaml'

    path_file1_simple_json = Path(Path.cwd(), path, file1_simple_json)
    path_file2_simple_json = Path(Path.cwd(), path, file2_simple_json)
    path_file1_nest_json = Path(Path.cwd(), path, file1_nest_json)
    path_file2_nest_json = Path(Path.cwd(), path, file2_nest_json)
    path_file1_json = Path(Path.cwd(), path, file1_json)
    path_file2_json = Path(Path.cwd(), path, file2_json)
    path_file1_simple_yml = Path(Path.cwd(), path, file1_simple_yml)
    path_file2_simple_yml = Path(Path.cwd(), path, file2_simple_yml)
    path_file1_nest_yml = Path(Path.cwd(), path, file1_nest_yml)
    path_file2_nest_yml = Path(Path.cwd(), path, file2_nest_yml)
    path_file1_yml = Path(Path.cwd(), path, file1_yml)
    path_file2_yml = Path(Path.cwd(), path, file2_yml)

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


def test_analyse_files(coll):
    result_json = analyse_diff_files(coll['file1_simple_json'],
                                     coll['file2_simple_json'])
    assert result_json == lists.simple
    result_yaml = analyse_diff_files(coll['file1_simple_yml'],
                                     coll['file2_simple_yml'])
    assert result_yaml == lists.simple

    result_json = analyse_diff_files(coll['file1_nest_json'],
                                     coll['file2_nest_json'])
    assert result_json == lists.nest
    result_yaml = analyse_diff_files(coll['file1_nest_yml'],
                                     coll['file2_nest_yml'])
    assert result_yaml == lists.nest


def test_stylish():
    assert format_stylish(lists.simple) == result_stylish_strings.simple
    assert format_stylish(lists.nest) == result_stylish_strings.nest
    assert format_stylish(lists.difficult) == result_stylish_strings.difficult


def test_plain():
    assert format_plain(lists.simple) == result_plain_strings.simple
    assert format_plain(lists.nest) == result_plain_strings.nest
    assert format_plain(lists.difficult) == result_plain_strings.difficult


def test_gendiff(coll):
    result_json = format_stylish(
        analyse_diff_files(coll['file1_json'], coll['file2_json']))
    assert result_json == result_stylish_strings.difficult

    result_yaml = format_stylish(
        analyse_diff_files(coll['file1_nest_yml'], coll['file2_nest_yml']))
    assert result_yaml == result_stylish_strings.nest

    result_json = format_plain(
        analyse_diff_files(coll['file1_json'], coll['file2_json']))
    assert result_json == result_plain_strings.difficult
