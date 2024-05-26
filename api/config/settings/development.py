from .base import *

INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar",
    "drf_spectacular",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS += [
    "127.0.0.1",
]

ROOT_URLCONF = "config.urls.development"

REST_FRAMEWORK.update({"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"})

SPECTACULAR_SETTINGS = {
    "TITLE": "Book Store API",
    "DESCRIPTION": "Simple API for book store.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
