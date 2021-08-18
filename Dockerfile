FROM python:3.8-slim

RUN apt-get update \
 && apt-get install -y libopencv-dev

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
