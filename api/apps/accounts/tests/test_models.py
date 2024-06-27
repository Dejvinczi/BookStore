import pytest


@pytest.mark.django_db
class TestUserModel:
    """Tests for the User model in the system."""

    def test_create_user(self, auth_user_model):
        """Test that the User model can be created."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)
        assert user.username == user_data["username"]
        assert user.email == user_data["email"]
        assert user.check_password(user_data["password"])

    def test_create_user_with_cart(self, auth_user_model):
        """Test that the User model can be created with a cart."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }

        user = auth_user_model.objects.create_user_with_cart(**user_data)
        assert user.username == user_data["username"]
        assert user.email == user_data["email"]
        assert user.check_password(user_data["password"])
        assert user.cart is not None

    def test_create_superuser(self, auth_user_model):
        """Test that the User model can be created as a superuser."""
        superuser_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
            "is_superuser": True,
        }
        user = auth_user_model.objects.create_user(**superuser_data)
        assert user.username == superuser_data["username"]
        assert user.email == superuser_data["email"]
        assert user.check_password(superuser_data["password"])
        assert user.is_superuser

    def test_str(self, auth_user_model):
        """Test that the User model returns the correct string representation."""
        user = auth_user_model.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com",
        )
        assert str(user) == user.username
