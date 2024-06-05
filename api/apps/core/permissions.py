from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """Custom permission to only allow owners of an object to edit it."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)
