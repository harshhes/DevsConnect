#!/usr/bin/env bash
pip install -r requirements.txt
# python devsconnect/manage.py collectstatic --no-input
python devsconnect/manage.py migrate