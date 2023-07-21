import json
import yaml


def read_files(args, format_):
    match format_:
        case 'json':
            first_file = json.load(open(args.first_file))
            second_file = json.load(open(args.second_file))
        case 'yaml':
            first_file = yaml.safe_load(open(args.first_file))
            second_file = yaml.safe_load(open(args.second_file))
        case _:
            return 'incorrect format'
    return first_file, second_file
