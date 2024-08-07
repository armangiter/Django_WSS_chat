FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/requirements.txt
WORKDIR /code/
RUN pip3 install -r requirements.txt
