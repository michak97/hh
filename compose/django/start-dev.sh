#!/bin/bash
python /app/manage.py migrate
python /app/manage.py collectstatic --noinput
python manage.py runserver_plus 0.0.0.0:5000
