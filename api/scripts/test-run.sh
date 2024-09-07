#!/bin/bash

# Apply database migrations
python manage.py migrate

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

# Run Django development server
python manage.py runserver 0.0.0.0:8000