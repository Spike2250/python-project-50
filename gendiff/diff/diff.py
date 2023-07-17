import json


def generate_diff(args) -> str:
    first_file, second_file = read_files(args)
    result = write_result(first_file, second_file)
    return result


def read_files(args):
    match args.format:
        case 'json':
            first_file = json.load(open(args.first_file))
            second_file = json.load(open(args.second_file))
        case _:
            return 'incorrect format'
    return first_file, second_file


def write_result(dict1, dict2) -> str:
    result = '{\n'

    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys = list(set(keys1 + keys2))
    keys.sort()

    for key in keys:
        if key in keys1 and key in keys2:
            if dict1[key] == dict2[key]:
                result += f"    {key}: {dict1[key]}\n"
            else:
                result += f"  - {key}: {dict1[key]}\n"
                result += f"  + {key}: {dict2[key]}\n"
        elif key in keys1 and key not in keys2:
            result += f"  - {key}: {dict1[key]}\n"
        else:
            result += f"  + {key}: {dict2[key]}\n"
    result += '}'
    return result
