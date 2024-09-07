#!/bin/bash

# Wait for a db service to be available
if ! wait-for-it.sh ${DATABASE_HOST}:${DATABASE_PORT} --timeout=30 --strict --; 
then
  echo "Database did not start in time. Exiting."
  exit 1
fi

# Apply database migrations
python manage.py migrate --noinput

# Create superuser (if exist - inform user that superuser already exists)
output=$(python manage.py createsuperuserwithcart --noinput 2>&1) || true

# Check if superuser already exists - if not create it
if echo "$output" | grep -q "CommandError: Error: That username is already taken."; then
    echo "Superuser already exists. Skipping creation."

elif [[ "$output" == *"Superuser created successfully."* ]]; then
    echo "Superuser created successfully."
else
    echo "$output"
    exit 1
fi

# Collect static files
python manage.py collectstatic --noinput

# Run Django production server
gunicorn config.wsgi:application --bind 0.0.0.0:8000