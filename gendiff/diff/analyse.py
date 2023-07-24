from collections import namedtuple


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
