from rest_framework.routers import SimpleRouter
from . import views

books_router = SimpleRouter(trailing_slash=False)
books_router.register("books", views.BookViewSet, basename="book")
books_router.register("authors", views.AuthorViewSet, basename="author")
books_router.register("genres", views.GenreViewSet, basename="genre")

app_name = "books"

urlpatterns = []

urlpatterns += books_router.urls
