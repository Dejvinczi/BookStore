"""Tests for the account API."""

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestRegisterView:
    """Tests for the register view."""

    REGISTER_URL = reverse("account:register")

    def test_register_user_success(self, api_client, auth_user_model):
        """Test that a new user can be registered successfully."""
        payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }

        response = api_client.post(self.REGISTER_URL, payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert auth_user_model.objects.filter(username=payload["username"]).count() == 1

    def test_register_user_existing_username_fail(self, api_client, auth_user_model):
        payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
        }
        auth_user_model.objects.create_user(**payload)

        response = api_client.post(self.REGISTER_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
