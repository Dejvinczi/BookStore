from rest_framework import serializers
from ..core.serializers import NestedPrimaryKeyRelatedField
from .models import Author, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "date_of_birth")


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genre model."""

    class Meta:
        model = Genre
        fields = ("id", "name")


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    authors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "authors", "genres", "publication_date")


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    authors = NestedPrimaryKeyRelatedField(
        AuthorSerializer,
        queryset=Author.objects.all(),
        many=True,
    )
    genres = NestedPrimaryKeyRelatedField(
        GenreSerializer,
        queryset=Genre.objects.all(),
        many=True,
    )

    class Meta:
        model = Book
        fields = ("id", "title", "authors", "genres", "publication_date")
