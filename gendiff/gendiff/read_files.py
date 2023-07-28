import json
import yaml


def read_file(file, format_):
    match format_:
        case 'json':
            file = json.load(open(file))
        case 'yaml':
            file = yaml.safe_load(open(file))
        case _:
            raise ValueError
    return file


def read_files(file1, file2, format_):
    return read_file(file1, format_), read_file(file2, format_)
