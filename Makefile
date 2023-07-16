install-poetry:
	@pip install poetry

install: install-poetry
	@poetry lock --no-update
	@poetry install

format:
	@echo "Start black execution:"
	@poetry run black ./app ./tests
	@echo "Finished black execution."
	@echo ""

	@echo "Start ruff fix execution:"
	@poetry run ruff check ./app ./tests --fix
	@echo "Finished ruff fix execution."
	@echo ""

check-lint:
	@echo "Start ruff check execution:"
	@poetry run ruff check ./app ./tests
	@echo "Finished ruff execution."
	@echo ""

	@echo "Start pylint execution:"
	@poetry run pylint ./app/
	@echo "Finished pylint execution."
	@echo ""

check-type:
	@echo "Start mypy execution:"
	@poetry run mypy --ignore-missing-imports ./app/
	@echo "Finished mypy execution."
	@echo ""

check-security:
	@echo "Start bandit execution:"
	@poetry run bandit -v -r ./app/ -c "pyproject.toml"
	@echo "Finished bandit execution."
	@echo ""

check-all:
	@echo "Start ruff check execution:"
	@poetry run ruff check ./app ./tests
	@echo "Finished ruff execution."
	@echo ""

	@echo "Start pylint execution:"
	@poetry run pylint ./app/
	@echo "Finished pylint execution."
	@echo ""

	@echo "Start mypy execution:"
	@poetry run mypy --ignore-missing-imports ./app/
	@echo "Finished mypy execution."
	@echo ""

	@echo "Start bandit execution:"
	@poetry run bandit -v -r ./app/ -c "pyproject.toml"
	@echo "Finished bandit execution."
	@echo ""

test: install
	@pytest -vv -rxs --capture=tee-sys

coverage: install
	@poetry run pytest -xs --cov app --cov-report html --cov-report=xml --cov-report term-missing --cov-config .coveragerc
