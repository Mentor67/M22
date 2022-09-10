# syntax=docker/dockerfile:1
FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /my_app_dir
WORKDIR /my_app_dir
COPY requirements.txt /my_app_dir/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /my_app_dir/