#!/usr/bin/env bash

APPS_LIST=(
  "comanage"
)

for app in "${APPS_LIST[@]}";do
    python manage.py makemigrations $app
done
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
python manage.py collectstatic --noinput

if [[ "${USE_DOT_VENV}" -eq 1 ]]; then
    uwsgi --uid ${UWSGI_UID:-1000} --gid ${UWSGI_GID:-1000}  --virtualenv ./.venv --ini uwsgi.ini
else
    uwsgi --uid ${UWSGI_UID:-1000} --gid ${UWSGI_GID:-1000}  --virtualenv ./venv --ini uwsgi.ini
fi