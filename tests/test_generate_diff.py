import pytest
import json
import yaml
from pathlib import Path
from tests.fixtures import result_gendiff as test_data

from gendiff.diff.diff import stringify, analyse_diff_files


@pytest.fixture
def coll():
    path = 'tests/fixtures/'
    # плоские структуры
    file1_s_json = 'file1_simple.json'
    file2_s_json = 'file2_simple.json'
    file1_s_yml = 'file1_simple.yaml'
    file2_s_yml = 'file2_simple.yaml'
    # вложенные структуры
    file1_json = 'file1.json'
    file2_json = 'file2.json'
    file1_yml = 'file1.yaml'
    file2_yml = 'file2.yaml'

    path_file1_s_json = Path(Path.cwd(), path, file1_s_json)
    path_file2_s_json = Path(Path.cwd(), path, file2_s_json)
    path_file1_s_yml = Path(Path.cwd(), path, file1_s_yml)
    path_file2_s_yml = Path(Path.cwd(), path, file2_s_yml)
    path_file1_json = Path(Path.cwd(), path, file1_json)
    path_file2_json = Path(Path.cwd(), path, file2_json)
    path_file1_yml = Path(Path.cwd(), path, file1_yml)
    path_file2_yml = Path(Path.cwd(), path, file2_yml)

    return {
        'file1_s_json': json.load(open(path_file1_s_json)),
        'file2_s_json': json.load(open(path_file2_s_json)),
        'file1_s_yml': yaml.safe_load(open(path_file1_s_yml)),
        'file2_s_yml': yaml.safe_load(open(path_file2_s_yml)),
        'file1_json': json.load(open(path_file1_json)),
        'file2_json': json.load(open(path_file2_json)),
        'file1_yml': yaml.safe_load(open(path_file1_yml)),
        'file2_yml': yaml.safe_load(open(path_file2_yml)),
    }


def test_analyse_files(coll):
    result_json = analyse_diff_files(coll['file1_s_json'],
                                     coll['file2_s_json'])
    assert result_json == test_data.result_list_1
    result_yaml = analyse_diff_files(coll['file1_s_yml'],
                                     coll['file2_s_yml'])
    assert result_yaml == test_data.result_list_1
    # result_json = analyse_diff_files(coll['file1_json'], coll['file2_json'])
    # assert result_json == test_data.result_list
    # result_yaml = analyse_diff_files(coll['file1_yml'], coll['file2_yml'])
    # assert result_yaml == test_data.result_list


def test_stringify():
    assert stringify(test_data.result_list_1) == test_data.result_string_1


def test_all(coll):
    result_json = stringify(
        analyse_diff_files(coll['file1_json'], coll['file2_json']))
    assert result_json == test_data.result_string_2
