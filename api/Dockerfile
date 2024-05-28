########################### BASE #################################
FROM python:3.12 as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /api

COPY /config /config
COPY /apps /apps
COPY /pyproject.toml /pyproject.toml
COPY /.flake8 /.flake8
COPY /conftest.py /conftest.py
COPY requirements/base.txt requirements/base.txt

RUN pip install -r requirements/base.txt

EXPOSE 8000

ENTRYPOINT ["bash"]


####################### DEVELOPMENT ##############################
FROM base as development

ENV DJANGO_SETTINGS_MODULE=config.settings.development
 
COPY requirements/development.txt requirements/development.txt
RUN pip install -r requirements/development.txt

COPY /scripts/dev-run.sh ./run.sh
RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]


######################## PRODUCTION ##############################
FROM base as production

ENV DJANGO_SETTINGS_MODULE=config.settings.production

COPY requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

COPY /scripts/prod-run.sh ./run.sh
RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]
