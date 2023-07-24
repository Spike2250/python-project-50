from gendiff.diff.read_files import read_file
from gendiff.diff.parse_file_format import parse_format
from gendiff.diff.formats.stylish import stylish
from gendiff.diff.formats.plain import plain

from gendiff.diff.analyse import analyse_diff_files


def generate_diff(args) -> str:
    try:
        file1 = read_file(args.first_file,
                          parse_format(args.first_file))
        file2 = read_file(args.second_file,
                          parse_format(args.second_file))
        analysed_list = analyse_diff_files(file1, file2)

        if args.format == 'plain':
            return plain(analysed_list)

        return stylish(analysed_list)

    except ValueError:
        return 'Format is not defined. Supported formats: "json", "yaml".'
