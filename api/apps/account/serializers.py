from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
