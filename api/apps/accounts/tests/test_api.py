"""Tests for the account API."""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


@pytest.mark.django_db
class TestRegisterView:
    """Tests for the register view."""

    REGISTER_URL = reverse("accounts:register")

    def test_register_user_success(self, api_client, auth_user_model):
        """Test that a new user can be registered successfully."""
        payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }

        response = api_client.post(self.REGISTER_URL, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED

        user = auth_user_model.objects.get(username=payload["username"])
        assert user.username == payload["username"]
        assert user.email == payload["email"]
        assert user.check_password(payload["password"])
        assert user.cart is not None

    def test_register_user_existing_username_fail(self, api_client, auth_user_model):
        """Test that registering a user with an existing username fails and returns a 400 status code."""
        payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        auth_user_model.objects.create_user(**payload)

        response = api_client.post(self.REGISTER_URL, payload, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestLoginView:
    """Tests for the login view."""

    LOGIN_URL = reverse("accounts:login")

    def test_login_user_success(self, api_client, auth_user_model):
        """Test that a user can login successfully."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)

        payload = {
            "username": user_data["username"],
            "password": user_data["password"],
        }

        response = api_client.post(self.LOGIN_URL, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

        access_token_obj = AccessToken(response.data["access"])

        assert access_token_obj["user_id"] == user.id

    def test_login_user_invalid_credentials_fail(self, api_client, auth_user_model):
        """Test that logging in with invalid credentials fails and returns a 401 status code."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        auth_user_model.objects.create_user(**user_data)

        payload = {
            "username": user_data["username"],
            "password": "invalidpassword",
        }

        response = api_client.post(self.LOGIN_URL, payload, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestLoginRefreshView:
    """Tests for the login (token) refresh view."""

    LOGIN_REFRESH_URL = reverse("accounts:login-refresh")

    def test_login_refresh_user_success(self, api_client, auth_user_model):
        """Test that a user can refresh their token."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)
        refresh_token = RefreshToken.for_user(user)

        payload = {"refresh": str(refresh_token)}

        response = api_client.post(self.LOGIN_REFRESH_URL, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data

        access_token_obj = AccessToken(response.data["access"])

        assert access_token_obj["user_id"] == user.id

    def test_login_refresh_user_invalid_token_fail(self, api_client, auth_user_model):
        """Test that logging in with an invalid token fails and returns a 401 status code."""
        payload = {"refresh": "invalidtoken"}

        response = api_client.post(self.LOGIN_REFRESH_URL, payload, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestLogoutView:

    LOGOUT_URL = reverse("accounts:logout")

    def test_logout_success(self, api_client, auth_user_model):
        """Test that a user can logout successfully."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)
        refresh_token = RefreshToken.for_user(user)

        payload = {"refresh": str(refresh_token)}

        response = api_client.post(self.LOGOUT_URL, payload, format="json")

        assert response.status_code == status.HTTP_200_OK

    def test_logout_with_blacklisted_token_fail(self, api_client, auth_user_model):
        """Test that logging out with a blacklisted token fails and returns a 401 status code."""
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()

        payload = {"refresh": str(refresh_token)}

        response = api_client.post(self.LOGOUT_URL, payload, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestProfileView:
    """Tests for the user profile view."""

    PROFILE_URL = reverse("accounts:profile")

    @pytest.fixture()
    def user(self, auth_user_model):
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        user = auth_user_model.objects.create_user(**user_data)
        return user

    def test_get_profile_unauthorized_fail(self, api_client):
        """Test that getting the user profile fails and returns a 401 status code."""
        response = api_client.get(self.PROFILE_URL, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_profile_unauthorized_fail(self, api_client):
        """Test that updating the user profile fails and returns a 401 status code."""
        response = api_client.put(self.PROFILE_URL, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_profile_success(self, api_client, user):
        """Test that a user can get their profile."""
        api_client.force_authenticate(user)

        response = api_client.get(self.PROFILE_URL, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username
        assert response.data["email"] == user.email

    def test_update_profile_success(self, api_client, user):
        """Test that a user can update their profile."""
        api_client.force_authenticate(user)

        payload = {
            "username": "newusername",
            "email": "newuser@example.com",
        }

        response = api_client.put(self.PROFILE_URL, payload, format="json")
        user.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == payload["username"]
        assert response.data["email"] == payload["email"]
        assert user.username == payload["username"]
        assert user.email == payload["email"]
