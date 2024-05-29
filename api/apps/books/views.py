from rest_framework import viewsets, permissions
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Author model."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        match self.action:
            case "list" | "retrieve":
                self.permission_classes = (permissions.AllowAny,)
            case _:
                self.permission_classes = (permissions.IsAdminUser,)

        return super().get_permissions()
