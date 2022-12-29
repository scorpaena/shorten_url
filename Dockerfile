FROM python:3.11

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    REDIS_URL="redis://redis:6379" \
    PYTHONPATH=":/code/api" \
    POETRY_VERSION=1.3.1

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false  \
    && poetry install --no-dev --no-root --no-interaction --no-ansi

COPY . ./
