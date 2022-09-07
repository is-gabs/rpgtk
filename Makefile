flake8:
	@poetry run flake8 --show-source tests rpgtk

check-python-import:
	@poetry run isort --check-only tests rpgtk

fix-python-import:
	@poetry run isort tests rpgtk

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@rm -rf dist/

lint: clean flake8 check-python-import

test: clean
	@poetry run pytest tests

requirements:
	@poetry install --no-root

coverage:
	@poetry run pytest --cov-config .coveragerc --cov rpgtk

release-patch:
	@poetry run bumpversion patch

release-minor:
	@poetry run bumpversion minor

release-major:
	@poetry run bumpversion major
