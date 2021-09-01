#!/usr/bin/env bash
# start-server.sh
#if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#    (cd web_app; python manage.py createsuperuser --no-input)
#fi
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=my_password \
DJANGO_SUPERUSER_USERNAME=my_user \
DJANGO_SUPERUSER_EMAIL=my_user@domain.com \
./manage.py createsuperuser \
--no-input
