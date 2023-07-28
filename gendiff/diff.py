from gendiff.utils.read_files import read_file
from gendiff.utils.formaters.plain import format_plain
from gendiff.utils.formaters.stylish import format_stylish
from gendiff.utils.formaters.json import format_json

from gendiff.utils.analyse import analyse_diff_files


def generate_diff(file1, file2, formater) -> str:
    try:
        file1 = read_file(file1)
        file2 = read_file(file2)
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
