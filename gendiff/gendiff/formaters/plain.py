import json


def format_plain(diff_data) -> str:  # noqa: C901
    lines = []

    def iter_(values, ancestry=[]):
        for i, item in enumerate(values):
            name = ".".join(ancestry + [item.key])
            value = adapt_value(item.value)

            if item.status == ' ' and isinstance(item.value, list):
                iter_(item.value, [name])
            elif item.status == '-':
                lines.append(f"Property '{name}' was removed")
            elif item.status == '+':
                if i != 0 and values[i - 1].key == item.key:
                    lines.pop()
                    prev_value = adapt_value(values[i - 1].value)
                    line = f"Property '{name}' was updated. "\
                           f"From {prev_value} to {value}"
                    lines.append(line)
                else:
                    line = f"Property '{name}' was added with value: {value}"
                    lines.append(line)
    iter_(diff_data)
    return '\n'.join(lines)


def adapt_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)