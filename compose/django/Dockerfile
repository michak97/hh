FROM python:3.13-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && echo Europe/Berlin > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
    build-essential python3-dev libmemcached-dev pkg-config libldap2-dev libsasl2-dev libzbar-dev ldap-utils tox lcov valgrind libpq-dev default-libmysqlclient-dev \
    && apt-get clean \
    && pip install uv \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsInportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 2000 django \
    && useradd -ms /bin/bash -g django django


COPY . /app

RUN if [ ! -d "app/staticfiles" ]; then mkdir app/staticfiles; fi 
RUN chown -R django /app
RUN chmod -R 777 app/staticfiles/

RUN uv pip install --system --upgrade pip \
    && uv pip install --no-cache-dir --system -r /app/pyproject.toml

COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

USER root

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]

