from rest_framework import viewsets, response, status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from apps.core.permissions import IsAdminOrReadOnly
from .models import Author, Genre, Book
from .serializers import (
    AuthorSerializer,
    GenreSerializer,
    BaseBookSerializer,
    BookListSerializer,
    BookRetrieveSerializer,
    BookCreateSerializer,
    BookUpdateSerializer,
    BookUploadImageSerializer,
)
from .filters import AuthorFilter, GenreFilter, BookFilter


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
    filterset_class = GenreFilter


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for the Book model."""

    queryset = Book.objects.all()
    serializer_class = BaseBookSerializer
    action_serializer_classes = {
        "list": BookListSerializer,
        "retrieve": BookRetrieveSerializer,
        "create": BookCreateSerializer,
        "update": BookUpdateSerializer,
        "partial_update": BookUpdateSerializer,
        "upload_image": BookUploadImageSerializer,
    }
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = BookFilter

    def get_queryset(self):
        """Get queryset based on action."""
        if self.action in ["list", "retrieve"]:
            return Book.objects.prefetch_related("authors", "genres").all()
        return self.queryset

    def get_serializer_class(self):
        """Get serializer class based on action."""
        serializer_class = self.action_serializer_classes.get(
            self.action, self.serializer_class
        )
        return serializer_class

    @action(
        detail=True,
        methods=["put"],
        url_path="image",
        parser_classes=[MultiPartParser],
    )
    def upload_image(self, request, *args, **kwargs):
        """Upload an image to the Book model."""
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
