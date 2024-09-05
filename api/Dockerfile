########################### BASE #################################
FROM python:3.12 AS base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /api

COPY config config
COPY apps apps
COPY requirements/base.txt requirements/base.txt
COPY manage.py manage.py

RUN pip install -r requirements/base.txt

EXPOSE 8000

ENTRYPOINT ["bash"]


####################### DEVELOPMENT ##############################
FROM base AS development

ENV DJANGO_SETTINGS_MODULE=config.settings.development

COPY conftest.py conftest.py
COPY pyproject.toml pyproject.toml
COPY .flake8 .flake8

COPY requirements/development.txt requirements/development.txt
RUN pip install -r requirements/development.txt

COPY scripts/dev-run.sh ./run.sh
COPY scripts/worker-run.sh ./worker-run.sh
RUN chmod +x ./run.sh
RUN chmod +x ./worker-run.sh

EXPOSE 5678

ENTRYPOINT ["./run.sh"]

####################### DEVELOPMENT ##############################
FROM base AS testing

ENV DJANGO_SETTINGS_MODULE=config.settings.testing
 
COPY conftest.py conftest.py
COPY pyproject.toml pyproject.toml
COPY .flake8 .flake8

COPY requirements/development.txt requirements/development.txt
RUN pip install -r requirements/development.txt

COPY scripts/dev-run.sh ./run.sh
COPY scripts/worker-run.sh ./worker-run.sh
RUN chmod +x ./run.sh
RUN chmod +x ./worker-run.sh

EXPOSE 5678

ENTRYPOINT ["./run.sh"]


######################## PRODUCTION ##############################
FROM base AS production

ENV DJANGO_SETTINGS_MODULE=config.settings.production

RUN find /api -type d -name 'tests' -exec rm -rf {} +

COPY requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

COPY /scripts/prod-run.sh ./run.sh
COPY scripts/worker-run.sh ./worker-run.sh
RUN chmod +x ./run.sh
RUN chmod +x ./worker-run.sh

ENTRYPOINT ["./run.sh"]
