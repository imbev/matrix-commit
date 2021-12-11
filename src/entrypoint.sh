#!/bin/bash
cd matrix-commit

python -m pip install poetry
python -m poetry install

python -m poetry run python src/action.py