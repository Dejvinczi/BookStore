#!/bin/bash

# Apply database migrations
python manage.py migrate

# Run Django development server
python manage.py runserver 0.0.0.0:8000