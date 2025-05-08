#!/usr/bin/env bash
# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# collect static files
python manage.py collectstatic --noinput
