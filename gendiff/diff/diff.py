from collections import namedtuple
from gendiff.diff.read_files import read_files
from gendiff.diff.parse_format import parse_format


def generate_diff(args) -> str:
    format_ = parse_format(args.first_file)
    first_file, second_file = read_files(args, format_)
    result = write_result(
        analyse_files(first_file, second_file)
    )
    return result


def analyse_files(dict1, dict2) -> list():
    result = []

    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys = list(set(keys1 + keys2))
    keys.sort()

    Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

    for key in keys:
        if key in keys1 and key in keys2:
            if dict1[key] == dict2[key]:
                result.append(Diff_str(' ', key, dict1[key]))
            else:
                result.append(Diff_str('-', key, dict1[key]))
                result.append(Diff_str('+', key, dict2[key]))
        elif key in keys1 and key not in keys2:
            result.append(Diff_str('-', key, dict1[key]))
        else:
            result.append(Diff_str('+', key, dict2[key]))
    return result


def write_result(analysed_list) -> str:
    result = '{\n'
    for t in analysed_list:
        result += f"  {t.status} {t.key}: {t.value}\n"
    result += '}'
    return result
