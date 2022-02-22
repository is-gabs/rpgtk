flake8:
	@poetry run flake8 --show-source .

check-python-import:
	@poetry run isort --check-only .

fix-python-import:
	@poetry run isort .

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@rm -rf dist/

lint: clean flake8 check-python-import

test_unit: clean
	@poetry run pytest

requirements:
	@poetry install
