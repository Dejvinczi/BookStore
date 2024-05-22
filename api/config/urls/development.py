from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .base import urlpatterns as base_urlpatterns

urlpatterns = base_urlpatterns + [
    path("debug/", include("debug_toolbar.urls")),
]
