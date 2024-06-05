from rest_framework import viewsets
from ..core.permissions import IsAdminOrReadOnly
from .models import Author, Genre
from .serializers import AuthorSerializer, GenreSerializer


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
