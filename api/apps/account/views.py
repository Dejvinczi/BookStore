from rest_framework import generics, permissions
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """View for user registration."""

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
