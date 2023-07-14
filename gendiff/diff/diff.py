import json


def generate_diff(args) -> str:
    first_file, second_file = read_files(args)

    result = '{\n'

    keys1 = list(first_file.keys())
    keys2 = list(second_file.keys())
    keys = list(set(keys1 + keys2))
    keys.sort()

    for key in keys:
        if key in keys1 and key in keys2:
            if first_file[key] == second_file[key]:
                result += f"    {key}: {first_file[key]}\n"
            else:
                result += f"  - {key}: {first_file[key]}\n"
                result += f"  + {key}: {second_file[key]}\n"
        elif key in keys1 and key not in keys2:
            result += f"  - {key}: {first_file[key]}\n"
        else:
            result += f"  + {key}: {second_file[key]}\n"
    result += '}'
    return result


def read_files(args):
    match args.format:
        case 'json':
            first_file = json.load(open(args.first_file))
            second_file = json.load(open(args.second_file))
        case _:
            return 'incorrect format'
    return first_file, second_file
