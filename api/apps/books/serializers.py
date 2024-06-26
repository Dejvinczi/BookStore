from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework import serializers
from .models import Author, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "date_of_birth")

    def validate_date_of_birth(self, value):
        """Validation of date of birth."""
        if value > timezone.now().date():
            raise serializers.ValidationError(
                {"date_of_birth": _("Date cannot be in the future.")}
            )
        return value


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genre model."""

    class Meta:
        model = Genre
        fields = ("id", "name")


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "authors",
            "genres",
            "publication_date",
            "image",
            "price",
        )
        extra_kwargs = {"image": {"read_only": True}}

    def validate_publication_date(self, value):
        """Validation of publication date."""
        if value > timezone.now().date():
            raise serializers.ValidationError(
                {"publication_date": _("Date cannot be in the future.")}
            )
        return value

    def validate_price(self, value):
        """Validation of price."""
        if value <= 0:
            raise serializers.ValidationError(
                {"price": _("Price must be a positive value.")}
            )
        return value


class BookListSerializer(BookSerializer):
    """Serializer for the Book model list."""

    authors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta(BookSerializer.Meta):
        pass


class BookRetrieveSerializer(BookSerializer):
    """Serializer for Book model details."""

    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta(BookSerializer.Meta):
        pass


class BookUploadImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading an image to the Book model."""

    class Meta:
        model = Book
        fields = ("image",)
