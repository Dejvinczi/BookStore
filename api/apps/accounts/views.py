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
    ProfileSerializer,
)


class RegisterView(generics.CreateAPIView):
    """View for user registration."""

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    """View for user login."""

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]


class LoginRefreshView(TokenRefreshView):
    """View for user login refresh."""

    serializer_class = LoginRefreshSerializer
    permission_classes = [permissions.AllowAny]


class LogoutView(TokenBlacklistView):
    """View for user logout (blacklist token refresh)."""

    permission_classes = [permissions.AllowAny]

    pass


class ProfileView(generics.RetrieveUpdateAPIView):
    """View for user profile."""

    serializer_class = ProfileSerializer

    def get_object(self):
        """Get current user object."""
        return self.request.user
