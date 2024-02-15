#!/bin/bash

# wait for Postgres to start
sleep 5

python manage.py migrate

python manage.py collectstatic --noinput

exec gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 1 --log-level=info
