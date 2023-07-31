from collections import namedtuple


def analyse_diff_files(dict1, dict2) -> list:  # noqa: C901
    """ """
    Diff = namedtuple('Diff', ('status', 'key', 'value'))

    ADDED = '+'
    REMOVED = '-'
    NOT_CHANGED = ' '

    def iter_(dict1, dict2):
        def not_changed_value(key):
            return Diff(NOT_CHANGED, key, dict1.get(key))

        def remove_value(key):
            return Diff(REMOVED, key, dict1.get(key))

        def add_value(key):
            return Diff(ADDED, key, dict2.get(key))

        def same_dicts_iter(key):
            return Diff(NOT_CHANGED, key,
                        iter_(dict1.get(key), dict2.get(key)))

        def remove_dict_iter(key):
            return Diff(REMOVED, key,
                        iter_(dict1.get(key), dict1.get(key)))

        def add_dict_iter(key):
            return Diff(ADDED, key,
                        iter_(dict2.get(key), dict2.get(key)))

        diff = []
        keys = list(set(list(dict1.keys()) + list(dict2.keys())))

        for key in sorted(keys):
            key_in_both_dict = key in dict1 and key in dict2
            values_are_same = dict1.get(key) == dict2.get(key)
            both_values_is_dict = all((isinstance(dict1.get(key), dict),
                                       isinstance(dict2.get(key), dict)))
            both_values_isnt_dict = all((not isinstance(dict1.get(key), dict),
                                         not isinstance(dict2.get(key), dict)))

            if key_in_both_dict:
                if values_are_same:
                    if both_values_isnt_dict:
                        diff.append(not_changed_value(key))
                    elif both_values_is_dict:
                        diff.append(same_dicts_iter(key))
                else:
                    if both_values_isnt_dict:
                        diff.append(remove_value(key))
                        diff.append(add_value(key))
                    elif both_values_is_dict:
                        diff.append(same_dicts_iter(key))
                    elif isinstance(dict1.get(key), dict):
                        diff.append(remove_dict_iter(key))
                        diff.append(add_value(key))
                    else:
                        diff.append(remove_value(key))
                        diff.append(add_dict_iter(key))
            elif key in dict1:
                if isinstance(dict1.get(key), dict):
                    diff.append(remove_dict_iter(key))
                else:
                    diff.append(remove_value(key))
            elif key in dict2:
                if isinstance(dict2.get(key), dict):
                    diff.append(add_dict_iter(key))
                else:
                    diff.append(add_value(key))
        return diff

    return iter_(dict1, dict2)
