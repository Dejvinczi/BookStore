from rest_framework import serializers
from .models import Author, Genre


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
