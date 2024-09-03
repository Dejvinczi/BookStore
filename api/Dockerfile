########################### BASE #################################
FROM python:3.12 AS base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /api

COPY config config
COPY apps apps
COPY conftest.py conftest.py
COPY requirements/base.txt requirements/base.txt
COPY manage.py manage.py

RUN pip install -r requirements/base.txt

EXPOSE 8000

ENTRYPOINT ["bash"]


####################### DEVELOPMENT ##############################
FROM base AS development

ENV DJANGO_SETTINGS_MODULE=config.settings.development
 
COPY pyproject.toml pyproject.toml
COPY .flake8 .flake8

COPY requirements/development.txt requirements/development.txt
RUN pip install -r requirements/development.txt

COPY scripts/dev-run.sh ./run.sh
RUN chmod +x ./run.sh

EXPOSE 5678

ENTRYPOINT ["./run.sh"]


######################## PRODUCTION ##############################
FROM base AS production

ENV DJANGO_SETTINGS_MODULE=config.settings.production

COPY requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

COPY /scripts/prod-run.sh ./run.sh
RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]
