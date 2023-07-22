from collections import namedtuple
import itertools
import json
from gendiff.diff.read_files import read_files
from gendiff.diff.parse_format import parse_format


def generate_diff(args) -> str:
    format_ = parse_format(args.first_file)
    first_file, second_file = read_files(args, format_)
    result = stringify(
        analyse_diff_files(first_file, second_file)
    )
    return result


# def analyse_diff_files(dict1, dict2) -> list:
#     Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

#     result = []

#     keys1 = list(dict1.keys())
#     keys2 = list(dict2.keys())
#     keys = list(set(keys1 + keys2))
#     keys.sort()

#     for key in keys:
#         if key in keys1 and key in keys2:
#             if dict1[key] == dict2[key]:
#                 result.append(Diff_str(' ', key, dict1[key]))
#             else:
#                 result.append(Diff_str('-', key, dict1[key]))
#                 result.append(Diff_str('+', key, dict2[key]))
#         elif key in keys1 and key not in keys2:
#             result.append(Diff_str('-', key, dict1[key]))
#         else:
#             result.append(Diff_str('+', key, dict2[key]))
#     return result


def analyse_diff_files(dict1, dict2) -> list:  # noqa: C901
    Diff_str = namedtuple('Diff_str', ('status', 'key', 'value'))

    def iter_(dict1, dict2):
        result = []
        keys1 = list(dict1.keys())
        keys2 = list(dict2.keys())
        keys = list(set(keys1 + keys2))
        keys.sort()

        for key in keys:
            key_in_both_dict = key in keys1 and key in keys2
            key_only_in_first_dict = key in keys1 and key not in keys2
            key_only_in_second_dict = key not in keys1 and key in keys2

            if key_in_both_dict:
                values_are_same = dict1[key] == dict2[key]
                both_values_is_dict = all((isinstance(dict1[key], dict),
                                           isinstance(dict2[key], dict)))
                both_values_isnt_dict = all((not isinstance(dict1[key], dict),
                                             not isinstance(dict2[key], dict)))
                any_value_is_dict = any((isinstance(dict1[key], dict),
                                         isinstance(dict2[key], dict)))

                if values_are_same:
                    if both_values_isnt_dict:
                        result.append(Diff_str(' ', key, dict1[key]))
                    elif both_values_is_dict:
                        result.append(
                            Diff_str(' ', key, iter_(dict1[key], dict2[key]))
                        )
                else:
                    if both_values_isnt_dict:
                        result.append(Diff_str('-', key, dict1[key]))
                        result.append(Diff_str('+', key, dict2[key]))
                    elif both_values_is_dict:
                        result.append(
                            Diff_str(' ', key, iter_(dict1[key], dict2[key]))
                        )
                    elif any_value_is_dict:
                        if isinstance(dict1[key], dict):
                            result.append(
                                Diff_str('-', key,
                                         iter_(dict1[key], dict1[key]))
                            )
                            result.append(Diff_str('+', key, dict2[key]))
                        else:
                            result.append(Diff_str('-', key, dict1[key]))
                            result.append(
                                Diff_str('+', key,
                                         iter_(dict2[key], dict2[key]))
                            )
            elif key_only_in_first_dict:
                if isinstance(dict1[key], dict):
                    result.append(
                        Diff_str('-', key, iter_(dict1[key], dict1[key]))
                    )
                else:
                    result.append(Diff_str('-', key, dict1[key]))
            elif key_only_in_second_dict:
                if isinstance(dict2[key], dict):
                    result.append(
                        Diff_str('+', key, iter_(dict2[key], dict2[key]))
                    )
                else:
                    result.append(Diff_str('+', key, dict2[key]))
        return result

    return iter_(dict1, dict2)


def stringify(value, replacer=' ', spaces_count=2) -> str:

    def iter_(value, depth):
        if not isinstance(value, list):
            if isinstance(value, bool) or value is None:
                return json.dumps(value)
            else:
                return str(value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for elem in value:
            line = f'{deep_indent}{elem.status} {elem.key}: '\
                   f'{iter_(elem.value, deep_indent_size + spaces_count)}'
            lines.append(line)
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
