import os
import pytest
import factory
import tempfile

from PIL import Image
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from apps.accounts.tests.factories import UserFactory, SuperuserFactory
from apps.books.tests.factories import AuthorFactory, GenreFactory, BookFactory
from apps.carts.tests.factories import CartFactory, CartItemFactory


@pytest.fixture
def auth_user_model():
    """
    Fixture to provide an User model that is active in this project.
    :return: User model
    """

    yield get_user_model()


@pytest.fixture
def user():
    yield UserFactory()


@pytest.fixture
def superuser():
    yield SuperuserFactory()


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


@pytest.fixture
def author_data():
    """
    Fixture for author data.

    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=AuthorFactory)


@pytest.fixture
def genre_data():
    """
    Fixture for genre data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=GenreFactory)


@pytest.fixture
def book_data():
    """
    Fixture for book data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=BookFactory)


@pytest.fixture
def author():
    """
    Fixture for author.
    :return: Author
    """
    return AuthorFactory()


@pytest.fixture
def genre():
    """
    Fixture for genre.
    :return: Genre
    """
    return GenreFactory()


@pytest.fixture
def book():
    """
    Fixture for book.
    :return: Book
    """
    return BookFactory()


@pytest.fixture
def author_factory():
    """
    Fixture for author factory.
    :return: AuthorFactory
    """
    return AuthorFactory


@pytest.fixture
def genre_factory():
    """
    Fixture for genre factory.
    :return: GenreFactory
    """
    return GenreFactory


@pytest.fixture
def book_factory():
    """
    Fixture for book factory.
    :return: BookFactory
    """
    return BookFactory


@pytest.fixture
def temp_image_file():
    """
    Fixture for temporary image file.
    :return: str
    """
    try:
        temp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)

        image = Image.new("RGB", (100, 100), color="red")
        image.save(temp, format="JPEG")

        temp.close()

        yield temp.name
    finally:
        try:
            os.remove(temp.name)
        except (AttributeError, FileNotFoundError):
            pass


@pytest.fixture
def cart_data():
    """
    Fixture for cart data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=CartFactory)


@pytest.fixture
def cart_item_data():
    """
    Fixture for cart item data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=CartItemFactory)


@pytest.fixture
def cart():
    """
    Fixture for CartFactory.
    :return: CartFactory
    """
    yield CartFactory()


@pytest.fixture
def cart_item():
    """
    Fixture for CartItemFactory.
    :return: CartItemFactory
    """
    yield CartItemFactory()


@pytest.fixture
def cart_factory():
    """
    Fixture for CartFactory.
    :return: CartFactory
    """
    return CartFactory


@pytest.fixture
def cart_item_factory():
    """
    Fixture for CartItemFactory.
    :return: CartItemFactory
    """
    return CartItemFactory
