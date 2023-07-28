import json
import yaml
from gendiff.utils.parse_file_format import parse_format


def read_file(file):
    format_ = parse_format(file)
    match format_:
        case 'json':
            file = json.load(open(file))
        case 'yaml':
            file = yaml.safe_load(open(file))
        case _:
            raise ValueError
    return file


def read_files(file1, file2):
    return read_file(file1), read_file(file2)
