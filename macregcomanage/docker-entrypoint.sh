#!/usr/bin/env bash
set -e

virtualenv -p /usr/local/bin/python .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

until [ $(pg_isready -h database -q)$? -eq 0 ]; do
    echo >&2 "Postgres is unavailable - sleeping"
    sleep 1
done

echo >&2 "Postgres is up - continuing"

if [[ ! -d "/code/sock" ]]; then
    mkdir -p /code/sock
fi
chown -R ${UWSGI_UID}:${UWSGI_GID} /code/sock

USE_DOT_VENV=1 ./run_uwsgi.sh

exec "$@"
