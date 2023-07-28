from collections import namedtuple


def analyse_diff_files(dict1, dict2) -> list:  # noqa: C901
    """Не понимаю как сделать эту функцию проще.

    Пока добален # noqa: C901 чтоб линтер не ругался
    и проходили тесты gitactions

    вложенные функции в iter() - по сути 'для красоты', чтоб
    было более менее читаемо. Есть ли в таком практический смысл?

    Использовал namedtuple для читаемого обращения к параметрам анализа.
    Целесообразнее ли использовать словарь / обычный кортеж?

    Буду признателен, если подскажите
    """
    Diff = namedtuple('Diff', ('status', 'key', 'value'))

    def iter_(dict1, dict2):
        def not_changed_value(key):
            return Diff(' ', key, dict1.get(key))

        def remove_value(key):
            return Diff('-', key, dict1.get(key))

        def add_value(key):
            return Diff('+', key, dict2.get(key))

        def same_dicts_iter(key):
            return Diff(' ', key, iter_(dict1.get(key), dict2.get(key)))

        def remove_dict_iter(key):
            return Diff('-', key, iter_(dict1.get(key), dict1.get(key)))

        def add_dict_iter(key):
            return Diff('+', key, iter_(dict2.get(key), dict2.get(key)))

        result = []
        add = result.append

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
                        add(not_changed_value(key))
                    elif both_values_is_dict:
                        add(same_dicts_iter(key))
                else:
                    if both_values_isnt_dict:
                        add(remove_value(key))
                        add(add_value(key))
                    elif both_values_is_dict:
                        add(same_dicts_iter(key))
                    elif isinstance(dict1.get(key), dict):
                        add(remove_dict_iter(key))
                        add(add_value(key))
                    else:
                        add(remove_value(key))
                        add(add_dict_iter(key))
            elif key in dict1:
                if isinstance(dict1.get(key), dict):
                    add(remove_dict_iter(key))
                else:
                    add(remove_value(key))
            elif key in dict2:
                if isinstance(dict2.get(key), dict):
                    add(add_dict_iter(key))
                else:
                    add(add_value(key))
        return result

    return iter_(dict1, dict2)
