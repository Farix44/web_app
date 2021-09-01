#!/usr/bin/env bash
# start-server.sh
#if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#    (cd web_app; python manage.py createsuperuser --no-input)
#fi
#python manage.py runserver 0.0.0.0:8000
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=admin \
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=admin@example.com \
./manage.py createsuperuser \
--no-input
