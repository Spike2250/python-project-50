import pytest
import json
import pathlib
from gendiff.diff.diff import write_result
from tests.fixtures import result_gendiff


@pytest.fixture
def coll():
    path = 'tests/fixtures/'
    file1 = 'file1.json'
    file2 = 'file2.json'
    path_file1 = pathlib.Path(pathlib.Path.cwd(), path, file1)
    path_file2 = pathlib.Path(pathlib.Path.cwd(), path, file2)
    return {
        'file1': json.load(open(path_file1)),
        'file2': json.load(open(path_file2))
    }


def test_write_result(coll):
    assert write_result(coll['file1'], coll['file2']) == result_gendiff.result
