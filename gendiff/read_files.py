from gendiff.parse import parse_file_format, parse_data


def read_file(file):
    format_ = parse_file_format(file)
    try:
        with open(file) as f:
            data = parse_data(f, format_)
    except FileNotFoundError:
        raise FileNotFoundError
    return data


def read_files(file1, file2):
    return read_file(file1), read_file(file2)
