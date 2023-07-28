#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.diff.gendiff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args)
    print(diff)


if __name__ == '__main__':
    main()
