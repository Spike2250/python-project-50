from gendiff.gendiff.parse_file_format import parse_format


def test_parse_format():
    assert parse_format('some_file.json') == 'json'
    assert parse_format('some.fi.le.json') == 'json'
    assert parse_format('kjbn/dsjkfn/rrrr.yml') == 'yaml'
    assert parse_format('some_ttt.yaml') == 'yaml'
    assert parse_format('df.kjfvkjbn/dsjkfn/ssss.rr') == ''
