from gendiff.diff.read_files import read_file, read_files
from gendiff.diff.parse_format import parse_format
from gendiff.diff.stringify import stringify
from gendiff.diff.analyse import analyse_diff_files


def generate_diff(args) -> str:
    try:
        if args.format == "stylish":
            file1 = read_file(args.first_file,
                              parse_format(args.first_file))
            file2 = read_file(args.second_file,
                              parse_format(args.second_file))
        else:
            file1, file2 = read_files(args.first_file,
                                      args.second_file,
                                      args.format)
        return stringify(analyse_diff_files(file1, file2))
    except ValueError:
        return 'Format is not defined. Supported formats: "json", "yaml".'
