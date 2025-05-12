#!/bin/sh
python /app/manage.py migrate
python /app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn --bind 0.0.0.0:8000 hh.wsgi
