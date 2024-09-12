########################### BASE #################################
FROM python:3.12 AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=config.settings.base

# Set working directory
WORKDIR /api

# Copy project files
COPY config ./config
COPY apps ./apps
COPY requirements/base.txt ./requirements/base.txt
COPY manage.py ./manage.py

# Create necessary directories and set permissions
RUN mkdir -p ./media ./static \
    && chmod -R 777 ./media ./static

# Install base Python dependencies
RUN pip install --no-cache-dir -r ./requirements/base.txt

# Create non-root user
RUN adduser --disabled-password --no-create-home api-user

# Set default port
EXPOSE 8000


####################### DEVELOPMENT ##############################
FROM base AS development

# Set development-specific environment variables
ENV DJANGO_SETTINGS_MODULE=config.settings.development
ENV PYDEVD_DISABLE_FILE_VALIDATION=1

# Copy development-specific files
COPY conftest.py ./conftest.py
COPY pyproject.toml ./pyproject.toml
COPY requirements/development.txt ./requirements/development.txt

# Install development dependencies
RUN pip install --no-cache-dir -r ./requirements/development.txt

# Copy and set up scripts
COPY scripts ./scripts
RUN chmod -R +x ./scripts

# Expose debugger port
EXPOSE 5678

# Set ownership and switch to non-root user
RUN chown -R api-user:api-user /api
USER api-user

# Update PATH with scripts directory
ENV PATH="$PATH:/api/scripts"

# Set entrypoint
ENTRYPOINT ["entrypoint-development.sh"]


####################### TESTING ##############################
FROM base AS testing

# Set testing-specific environment variables
ENV DJANGO_SETTINGS_MODULE=config.settings.testing
ENV PYDEVD_DISABLE_FILE_VALIDATION=1

# Copy testing-specific files
COPY conftest.py ./conftest.py
COPY pyproject.toml ./pyproject.toml
COPY requirements/testing.txt ./requirements/testing.txt

# Install testing dependencies
RUN pip install --no-cache-dir -r ./requirements/testing.txt

# Copy and set up scripts
COPY scripts/entrypoint-development.sh ./scripts/entrypoint-development.sh
COPY scripts/entrypoint-celery-worker.sh ./scripts/entrypoint-celery-worker.sh 
COPY scripts/wait-for-it.sh ./scripts/wait-for-it.sh
RUN chmod -R +x ./scripts

# Set ownership and switch to non-root user
RUN chown -R api-user:api-user /api
USER api-user

# Update PATH with scripts directory
ENV PATH="$PATH:/api/scripts"

# Set entrypoint
ENTRYPOINT ["entrypoint-testing.sh"]


######################## PRODUCTION ##############################
FROM base AS production

# Set production-specific environment variables
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Remove test directories
RUN find /api -type d -name 'tests' -exec rm -rf {} +

# Copy production-specific files
COPY requirements/production.txt ./requirements/production.txt

# Install production dependencies
RUN pip install -r ./requirements/production.txt

# Copy and set up scripts
COPY scripts/entrypoint-production.sh ./scripts/entrypoint-production.sh
COPY scripts/entrypoint-celery-worker.sh ./scripts/entrypoint-celery-worker.sh 
COPY scripts/wait-for-it.sh ./scripts/wait-for-it.sh
RUN chmod -R +x ./scripts

# Set ownership and switch to non-root user
RUN chown -R api-user:api-user /api
USER api-user

# Update PATH with scripts directory
ENV PATH="$PATH:/api/scripts"

# Set entrypoint
ENTRYPOINT ["entrypoint-production.sh"]
