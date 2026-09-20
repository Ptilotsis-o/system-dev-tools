.PHONY: all test clean

all: dist/demo-0.1.0-py3-none-any.whl

dist/demo-0.1.0-py3-none-any.whl: src/demo/core.py pyproject.toml
	python -m build

test: all
	pytest -v

clean:
	rm -rf dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
