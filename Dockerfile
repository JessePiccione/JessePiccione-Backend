# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

ARG PYTHON_VERSION=3.11.7
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONUNBUFFERED 1
RUN mkdir /JessePiccione
WORKDIR /JessePiccione
COPY requirements.txt /JessePiccione/
RUN pip install --user -r requirements.txt
COPY . /JessePiccione/
CMD python manage.py runserver 0.0.0.0:80