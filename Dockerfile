FROM python:3.10.5

WORKDIR /app

ENV PYTHONUNBUFFERED=1
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

COPY . /app
