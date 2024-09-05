from .base import *  # NOQA

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

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
ROOT_URLCONF = "config.urls.development"

REST_FRAMEWORK.update(
    {
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
        "DEFAULT_AUTHENTICATION_CLASSES": REST_FRAMEWORK[
            "DEFAULT_AUTHENTICATION_CLASSES"
        ]
        + ["rest_framework.authentication.SessionAuthentication"],
        "DEFAULT_RENDERER_CLASSES": REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"]
        + ["rest_framework.renderers.BrowsableAPIRenderer"],
        "DEFAULT_PARSER_CLASSES": REST_FRAMEWORK["DEFAULT_PARSER_CLASSES"]
        + ["rest_framework.parsers.MultiPartParser"],
    },
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Book Store API",
    "DESCRIPTION": "Simple API for book store.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CELERY_TASK_ALWAYS_EAGER = True
