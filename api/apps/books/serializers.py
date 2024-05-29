from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.Serializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "date_of_birth")
