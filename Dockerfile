FROM python:3.11-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY spin_service /spin_service
WORKDIR /spin_service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password spin-user

USER spin-user