import pytest
import json
from gendiff.diff.diff import write_result
from tests.fixtures import result_gendiff


@pytest.fixture
def coll():
    path = 'tests/fixtures/'
    return {
        'file1': json.load(open(f'{path}file1.json')),
        'file2': json.load(open(f'{path}file2.json'))
    }


def test_write_result(coll):
    assert write_result(coll['file1'], coll['file2']) == result_gendiff.result
