build:
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

tests:
	poetry run pytest tests -vv

lint:
	poetry run flake8 page_loader

test-coverage:
	poetry run pytest --cov page_loader --cov-report xml

install:
	poetry install

poetry-install:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py --uninstall | python3 -
	poetry config virtualenvs.in-project true

rebuild:
	make build
	make package-install

.PHONY: build package-install lint install poetry-install tests test-coverage rebuild
