from django.db import transaction
from django.contrib.auth.models import AbstractUser, UserManager
from apps.carts.models import Cart


class CustomUserManager(UserManager):
    """Custom user manager."""

    def create_user_with_cart(self, username, email, password, **extra_fields):
        """Create and save a user with the given username, email, and password."""
        with transaction.atomic():
            user = self.create_user(username, email, password, **extra_fields)
            Cart.objects.create(user=user)
            return user


class User(AbstractUser):
    """User model in the system."""

    objects = CustomUserManager()

    def __str__(self):
        return self.username
