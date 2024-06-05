#!/bin/bash

# Apply database migrations
python manage.py migrate

# Run Django development server
python -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000