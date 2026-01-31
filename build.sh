#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

# collectstatic is required for WhiteNoise (serving static files in production)
python manage.py collectstatic --noinput

# Tip: run database migrations from Render Shell after first deploy:
#   python manage.py migrate
