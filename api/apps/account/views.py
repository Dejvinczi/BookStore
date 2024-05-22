from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    """View for user registration."""

    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
