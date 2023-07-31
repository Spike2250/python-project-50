from gendiff.formaters.plain import to_string


def test_to_string():
    assert to_string("value") == "'value'"
    assert to_string(40) == '40'
    assert to_string(True) == 'true'
    assert to_string([1, 2]) == '[complex value]'
    assert to_string(None) == 'null'
