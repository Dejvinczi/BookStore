from rest_framework import viewsets
from apps.core.permissions import IsAdminOrReadOnly
from .models import Author, Genre, Book
from .serializers import (
    AuthorSerializer,
    GenreSerializer,
    BookSerializer,
    BookDetailSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Author model."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for the Genre model."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for the Book model."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    detail_serializer_class = BookDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        """Get serializer class based on action."""
        if self.action == "list":
            return self.serializer_class
        return self.detail_serializer_class
