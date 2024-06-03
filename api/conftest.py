import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model


@pytest.fixture
def auth_user_model():
    """
    Fixture to provide an User model that is active in this project.
    :return: User model
    """

    yield get_user_model()


@pytest.fixture
def superuser(db, auth_user_model):
    """
    Fixture to provide an admin user that is active in this project.
    :return: User model
    """

    yield auth_user_model.objects.create_superuser(
        username="testadmin",
        password="testpassword",
        email="testadmin@example.com",
    )


@pytest.fixture
def user(db, auth_user_model):
    """
    Fixture to provide an user that is active in this project.
    :return: User model
    """

    yield auth_user_model.objects.create_user(
        username="testuser",
        password="testpassword",
        email="testuser@example.com",
    )


@pytest.fixture
def api_client():
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()


@pytest.fixture
def auth_api_client(api_client, user):
    """
    Fixture to provide an API client for authenticated users
    :return: APIClient
    """
    access_token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    yield api_client


@pytest.fixture
def admin_api_client(api_client, superuser):
    """
    Fixture to provide an API client for admin users
    :return: APIClient
    """
    access_token = AccessToken.for_user(superuser)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    yield api_client
