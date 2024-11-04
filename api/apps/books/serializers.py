from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework import serializers
from .models import Author, Genre, Book


class BaseAuthorSerializer(serializers.ModelSerializer):
    """Base serializer for the Author model."""

    class Meta:
        model = Author
        fields = "__all__"

    def validate_date_of_birth(self, value):
        """Validation of date of birth."""
        if value > timezone.now().date():
            raise serializers.ValidationError(_("Date cannot be in the future."))
        return value


class AuthorSerializer(BaseAuthorSerializer):
    """Serializer for the Author model."""

    class Meta(BaseAuthorSerializer.Meta):
        fields = ("id", "first_name", "last_name", "date_of_birth")


class BaseGenreSerializer(serializers.ModelSerializer):
    """Base serializer for the Genre model."""

    class Meta:
        model = Genre
        fields = "__all__"


class GenreSerializer(BaseGenreSerializer):
    """Serializer for the Genre model."""

    class Meta(BaseGenreSerializer.Meta):
        fields = ("id", "name")


class BaseBookSerializer(serializers.ModelSerializer):
    """Base serializer for the Book model."""

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_date(self, value):
        """Validation of publication date."""
        if value > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value

    def validate_price(self, value):
        """Validation of price."""
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value


class BookCreateSerializer(BaseBookSerializer):
    """Serializer for the Book model creation."""

    class Meta(BaseBookSerializer.Meta):
        fields = (
            "title",
            "authors",
            "genres",
            "publication_date",
            "price",
        )


class BookListSerializer(BaseBookSerializer):
    """Serializer for the Book model listing."""

    authors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta(BaseBookSerializer.Meta):
        fields = (
            "id",
            "title",
            "authors",
            "genres",
            "publication_date",
            "image",
            "price",
        )
        read_only_fields = fields


class BookRetrieveSerializer(BaseBookSerializer):
    """Serializer for the Book model retrieving."""

    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta(BaseBookSerializer.Meta):
        fields = (
            "id",
            "title",
            "authors",
            "genres",
            "publication_date",
            "image",
            "price",
        )
        read_only_fields = fields


class BookUpdateSerializer(BaseBookSerializer):
    """Serializer for Book model updating."""

    class Meta(BaseBookSerializer.Meta):
        fields = (
            "id",
            "title",
            "authors",
            "genres",
            "publication_date",
            "price",
        )


class BookUploadImageSerializer(BaseBookSerializer):
    """Serializer for uploading an image to the Book model."""

    class Meta(BaseBookSerializer.Meta):
        fields = ("image",)
