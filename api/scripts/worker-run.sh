#!/bin/bash

# Wait for a db service to be available
if ! wait-for-it.sh ${DATABASE_HOST}:${DATABASE_PORT} --timeout=30 --strict --; 
then
  echo "Database did not start in time. Exiting."
  exit 1
fi

# Start celery
celery -A config worker --loglevel=info --concurrency 1 -E