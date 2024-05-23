import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()


@pytest.fixture(scope="session")
def auth_user_model():
    """
    Fixture to provide an User model that is active in this project.
    :return: User model
    """

    yield get_user_model()
