from gendiff.read_files import read_file
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.json import format_json

from gendiff.diff import analyse_diff_files


def generate_diff(path_to_file1, path_to_file2, formater='stylish') -> str:
    try:
        file1 = read_file(path_to_file1)
        file2 = read_file(path_to_file2)
        analysed_list = analyse_diff_files(file1, file2)

        if formater == 'plain':
            return format_plain(analysed_list)
        elif formater == 'json':
            return format_json(analysed_list)

        return format_stylish(analysed_list)

    except ValueError:
        msg = 'File\'s format is not defined. '\
              'Supported formats: "json", "yaml".'
        return msg
    except FileNotFoundError:
        msg = 'File/files not found. Try again.'
        return msg
