FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /news
WORKDIR /news
COPY requirements.txt /news/
RUN pip install -r requirements.txt
COPY . /news/
