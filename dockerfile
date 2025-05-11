FROM python:3.10.17-alpine3.21

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev python3-dev mariadb-dev

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

