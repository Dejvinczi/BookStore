from rest_framework import generics, permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    LoginRefreshSerializer,
)


class RegisterView(generics.CreateAPIView):
    """View for user registration."""

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    """View for user login."""

    serializer_class = LoginSerializer


class LoginRefreshView(TokenRefreshView):
    serializer_class = LoginRefreshSerializer


class LogoutView(TokenBlacklistView):
    pass
