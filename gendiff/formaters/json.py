import json
from collections import namedtuple


def format_json(diff_data):
    return json.dumps(diff_data, indent=2)


def return_original_structure(result_of_format_json):
    """Принимает результат format_json
    возвращает список именованных кортежей"""
    Diff = namedtuple('Diff', ('status', 'key', 'value'))

    list_of_tuples = json.loads(result_of_format_json)

    def iter_(list_):
        new_list = []
        for tuple_ in list_:
            if not isinstance(tuple_[2], list):
                new_list.append(Diff(*tuple_))
            else:
                new_list.append(Diff(tuple_[0],
                                     tuple_[1],
                                     iter_(tuple_[2])))
        return new_list

    result = iter_(list_of_tuples)
    return result
