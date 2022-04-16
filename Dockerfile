# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN pip3 install flask flask-wtf email_validator requests flask-login flask-sqlalchemy
COPY app.py app.py
CMD python app.py
