#!/usr/bin/env bash
set -e

echo "=== Running Ruff Format (Check) ==="
ruff format --check .

echo "=== Running Ruff Lint ==="
ruff check .

echo "=== Running Pytest ==="
pytest -v

echo "All checks passed"
