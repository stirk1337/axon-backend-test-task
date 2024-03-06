FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN  pip install pipenv \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt

COPY . .
