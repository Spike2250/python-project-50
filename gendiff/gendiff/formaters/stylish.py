import itertools
import json


def format_stylish(diff_data, replacer=' ', spaces_count=2) -> str:
    def iter_(value, depth):
        if not isinstance(value, list):
            return adapt_value(value)

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

    def adapt_value(value):
        if isinstance(value, bool) or value is None:
            return json.dumps(value)
        else:
            return str(value)

    return iter_(diff_data, 0)
