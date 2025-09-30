#!/bin/bash

# Exit on error
set -e

# Display Python version
python --version

# Run Ruff lint
echo "Running Ruff lint..."
ruff check --output-format=github . || { echo "Ruff lint failed"; exit 1; }

# Run Ruff format check
echo "Running Ruff format check..."
ruff format --check . || { echo "Ruff format check failed"; exit 1; }

# Run Flake8
echo "Running Flake8..."
flake8 . --count --doctests --show-source --statistics || { echo "Flake8 check failed"; exit 1; }

# Run Pylint
echo "Running Pylint..."
pylint --verbose $(find . -name "*.py" ! -path "*/.venv/*" ! -path "*/venv/*") --rcfile=.pylintrc  || { echo "Pylint check failed"; exit 1; }

# Run Pytest
echo "Running Pytest..."
pytest . --verbose --ignore=solutions --log-cli-level=INFO  || { echo "Pytest check failed"; exit 1; }
