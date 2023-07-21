def parse_format(name_file):
    ending = name_file.split('.')[-1]
    format_ = ''
    if ending in ('yml', 'yaml'):
        format_ = 'yaml'
    elif ending == 'json':
        format_ = 'json'

    return format_
