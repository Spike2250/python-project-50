install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

check:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff

test-run-json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test-run-json-plain:
	poetry run gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json

test-run-json-json:
	poetry run gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json

test-run-yaml:
	poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml

test-run-yaml-plain:
	poetry run gendiff --format plain tests/fixtures/file1.yaml tests/fixtures/file2.yaml

test-run-yaml-json:
	poetry run gendiff --format json tests/fixtures/file1.yaml tests/fixtures/file2.yaml
