FROM python:3.9

COPY pyproject.toml /matrix-commit/pyproject.toml
COPY poetry.lock /matrix-commit/poetry.lock
COPY matrix-commit/ /matrix-commit/matrix-commit/

ENTRYPOINT ["/matrix-commit/matrix-commit/entrypoint.sh"]