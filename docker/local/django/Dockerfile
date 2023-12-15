FROM python:3.11.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

LABEL maintainer='jason.kei.hall@gmail.com'
LABEL decription="Development image for Real Estate Project"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt 

RUN pip install -r requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]