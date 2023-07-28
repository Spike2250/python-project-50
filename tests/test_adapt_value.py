from gendiff.utils.formaters.plain import adapt_value


def test_adapt_value():
    assert adapt_value("value") == "'value'"
    assert adapt_value(40) == '40'
    assert adapt_value(True) == 'true'
    assert adapt_value([1, 2]) == '[complex value]'
    assert adapt_value(None) == 'null'
