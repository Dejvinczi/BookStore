############################### BASE BUILDER ####################################
FROM python:3.12-slim AS base-builder

# Set Python and pip environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/opt/venv \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies and clean up in the same layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv $VIRTUAL_ENV

# Add virtual env to path
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create working directory
WORKDIR /api

# Copy requirements files
COPY requirements/ requirements/

# Install base requirements
RUN pip install --no-cache-dir -r requirements/base.txt


########################### DEVELOPMENT BUILDER #################################
FROM base-builder AS dev-builder
RUN pip install --no-cache-dir -r requirements/development.txt


############################# TESTING BUILDER ###################################
FROM base-builder AS test-builder
RUN pip install --no-cache-dir -r requirements/testing.txt


########################### PRODUCTION BUILDER #################################
FROM base-builder AS prod-builder
RUN pip install --no-cache-dir -r requirements/production.txt


################################### BASE #########################################
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/opt/venv \
    DJANGO_SETTINGS_MODULE=config.settings.base

# Install runtime dependencies and create user in the same layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r docker --gid 1000 \
    && useradd -r -g docker --uid 1000 -s /bin/bash docker \
    && mkdir -p /api/media/books /api/static \
    && chown -R docker:docker /api \
    && chmod -R 775 /api/media /api/static

WORKDIR /api

# Copy virtual environment from builder
COPY --from=base-builder --chown=docker:docker /opt/venv /opt/venv

# Copy common scripts first
COPY --chown=docker:docker scripts ./scripts
RUN chmod -R +x ./scripts

# Now we can safely add scripts to PATH
ENV PATH="$VIRTUAL_ENV/bin:/api/scripts:$PATH"

# Copy project files
COPY --chown=docker:docker config ./config
COPY --chown=docker:docker apps ./apps
COPY --chown=docker:docker manage.py ./manage.py

# Set default port
EXPOSE 8000

############################### DEVELOPMENT ######################################
FROM base AS development
ENV DJANGO_SETTINGS_MODULE=config.settings.development \
    PYDEVD_DISABLE_FILE_VALIDATION=1

# Copy virtual environment from development builder
COPY --from=dev-builder --chown=docker:docker /opt/venv /opt/venv

# Copy development-specific files
COPY --chown=docker:docker conftest.py pyproject.toml ./

# Copy and set up scripts
COPY --chown=docker:docker scripts ./scripts
RUN chmod -R +x ./scripts

# Expose debugger port
EXPOSE 5678

USER docker:docker
ENTRYPOINT ["entrypoint-development.sh"]


############################### TESTING #########################################
FROM base AS testing
ENV DJANGO_SETTINGS_MODULE=config.settings.testing \
    PYDEVD_DISABLE_FILE_VALIDATION=1

# Copy virtual environment from testing builder
COPY --from=test-builder --chown=docker:docker /opt/venv /opt/venv

# Copy testing-specific files
COPY --chown=docker:docker conftest.py pyproject.toml ./
COPY --chown=docker:docker scripts/entrypoint-testing.sh \
    scripts/entrypoint-celery-worker.sh \
    scripts/wait-for-it.sh \
    ./scripts/

RUN chmod -R +x ./scripts

USER docker:docker

ENTRYPOINT ["entrypoint-testing.sh"]


########################### PRODUCTION ##########################################
FROM base AS production
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Copy virtual environment from production builder
COPY --from=prod-builder --chown=docker:docker /opt/venv /opt/venv

# Remove test directories
RUN find /api -type d -name 'tests' -exec rm -rf {} +

# Copy production scripts
COPY --chown=docker:docker scripts/entrypoint-production.sh \
    scripts/entrypoint-celery-worker.sh \
    scripts/wait-for-it.sh \
    ./scripts/

RUN chmod -R +x ./scripts

USER docker:docker

ENTRYPOINT ["entrypoint-production.sh"]
