from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("authors", views.AuthorViewSet, basename="author")

app_name = "books"

urlpatterns = [
    path("", include(router.urls)),
]