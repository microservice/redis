FROM        python:3.6-alpine

RUN         MKDIR /app
ADD         requirements.txt /app
RUN         pip install -r /app/requirements.txt
ADD         app.py /app

ENTRYPOINT  ["python", "/app/app.py"]
