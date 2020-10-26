FROM python:3.9-alpine

RUN         apk update
RUN         apk add redis
RUN         mkdir /app
RUN         mkdir /db
ADD         requirements.txt /app
RUN         pip install -r /app/requirements.txt
ADD         start.sh /app
ADD         oms /app/oms
ADD         redis.conf /app

ENTRYPOINT  ["/bin/sh", "/app/start.sh"]
