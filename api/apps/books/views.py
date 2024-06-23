from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from apps.core.permissions import IsAdminOrReadOnly
from .models import Author, Genre, Book
from .serializers import (
    AuthorSerializer,
    GenreSerializer,
    BookSerializer,
    BookDetailSerializer,
    BookUploadImageSerializer,
)
from .filters import AuthorFilter


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Author model."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = AuthorFilter


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
        if self.action == "upload_image":
            return BookUploadImageSerializer
        return self.detail_serializer_class

    @action(
        detail=True,
        methods=["put"],
        url_path="upload-image",
        serializer_class=BookUploadImageSerializer,
    )
    def upload_image(self, request, *args, **kwargs):
        """Upload an image to the Book model."""
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
