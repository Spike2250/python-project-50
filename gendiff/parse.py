import json
import yaml


def parse_file_format(name_file):
    ending = name_file.split('.')[-1]
    format_ = ''
    if ending in ('yml', 'yaml'):
        format_ = 'yaml'
    elif ending == 'json':
        format_ = 'json'

    return format_


def parse_data(data, format_):
    match format_:
        case 'json':
            try:
                data = json.load(data)
            except AttributeError:
                data = json.loads(data)
        case 'yaml':
            data = yaml.safe_load(data)
        case _:
            raise ValueError
    return data
