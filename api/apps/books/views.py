from rest_framework import viewsets, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Author model."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_authenticators(self):
        if self.request is None or self.request.method in permissions.SAFE_METHODS:
            return []
        return [JWTAuthentication()]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]

        return [permissions.IsAdminUser()]
