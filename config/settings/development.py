from decouple import config
from .base import *

SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)

LOCAL_INSTALLED_APPS = []
INSTALLED_APPS = INSTALLED_APPS + LOCAL_INSTALLED_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("DATABASE_USER_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT"),
    }
}
