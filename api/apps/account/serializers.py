from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """Serializer for user login."""

    pass


class LoginRefreshSerializer(TokenRefreshSerializer):
    """Serializer for user login refresh."""

    pass
