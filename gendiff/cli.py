import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file',
                        help='path to first file')
    parser.add_argument('second_file',
                        help='path to second file')
    parser.add_argument('-f', '--format',
                        choices=['json', 'plain'],
                        default='json',
                        help='set format of output')
    return parser.parse_args()
