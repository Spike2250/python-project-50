import pytest
from gendiff.utils.read_files import read_file, read_files


def test_read_files():
    path_file1_json = 'tests/fixtures/file1.json'
    path_file2_json = 'tests/fixtures/file2.json'

    path_file1_yaml = 'tests/fixtures/file1.yaml'
    path_file2_yaml = 'tests/fixtures/file2.yaml'

    file1 = read_file(path_file1_json)
    file2 = read_file(path_file2_json)
    assert isinstance(file1, dict)
    assert isinstance(file2, dict)

    file1 = read_file(path_file1_yaml)
    file2 = read_file(path_file2_yaml)
    assert isinstance(file1, dict)
    assert isinstance(file2, dict)

    with pytest.raises(ValueError):
        read_file('fsdfdsdfs.exe')
    with pytest.raises(ValueError):
        read_file('dfgkjdbnfg.js')

    file1, file2 = read_files(path_file1_json, path_file2_json)
    assert isinstance(file1, dict) == isinstance(file2, dict)
