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

        def iter_key_in_both_dict(key, values_are_same,
                                  both_values_is_dict,
                                  both_values_isnt_dict):
            if values_are_same:
                iter_values_are_same(key, both_values_is_dict,
                                     both_values_isnt_dict)
            else:
                iter_values_arent_same(key, both_values_is_dict,
                                       both_values_isnt_dict)

        def iter_values_are_same(key, both_values_is_dict,
                                 both_values_isnt_dict):
            if both_values_isnt_dict:
                diff.append(not_changed_value(key))
            elif both_values_is_dict:
                diff.append(same_dicts_iter(key))

        def iter_values_arent_same(key, both_values_is_dict,
                                   both_values_isnt_dict):
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

        def iter_key_in_dict1(key):
            if isinstance(dict1.get(key), dict):
                diff.append(remove_dict_iter(key))
            else:
                diff.append(remove_value(key))

        def iter_key_in_dict2(key):
            if isinstance(dict2.get(key), dict):
                diff.append(add_dict_iter(key))
            else:
                diff.append(add_value(key))

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
                iter_key_in_both_dict(key, values_are_same,
                                      both_values_is_dict,
                                      both_values_isnt_dict)
            elif key in dict1:
                iter_key_in_dict1(key)
            elif key in dict2:
                iter_key_in_dict2(key)
        return diff

    return iter_(dict1, dict2)
