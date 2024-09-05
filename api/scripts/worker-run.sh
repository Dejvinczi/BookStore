#!/bin/bash

celery -A config worker --loglevel=info --concurrency 1 -E