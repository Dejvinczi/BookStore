import factory
from django.contrib.auth import get_user_model
import factory.fuzzy

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for User model."""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"User {n}")
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.django.Password("samplepassword")


class SuperuserFactory(UserFactory):
    is_superuser = True
    is_staff = True
    is_active = True
