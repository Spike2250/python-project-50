## Difference generator
> A command line tool to calculate the difference between two data structures. Runs from the command line, compares two configuration files and shows a difference. Working with JSON and YAML. Provides output in stylish, plain and json format.
### Usage:
#### Help: 
```sh
$ gendiff -h
```
#### Running:
```sh
$ gendiff <file_path1> <file_path2> --format <format>
```
##### format - optional parameter, default value is 'stylish'. Possible values: 'stylish', 'plain', 'json'.
### Setup 
#### Using Makefile:
```sh
$ make install
```
```sh
$ make build
```
```sh
$ make package-install
```
### Asciinemas


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Spike2250/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Spike2250/python-project-50/actions)  [![main](https://github.com/Spike2250/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Spike2250/python-project-50/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/Spike2250/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/cbda8f3b8956884a7c5f/maintainability" /></a>
<a href="https://codeclimate.com/github/Spike2250/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/cbda8f3b8956884a7c5f/test_coverage" /></a>