import os
import pytest
import factory
import tempfile
from PIL import Image
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

# Models
from apps.books.models import Author, Genre, Book
from apps.carts.models import Cart, CartItem
from apps.orders.models import Order, OrderItem

# Factories
from apps.accounts.tests.factories import UserFactory, SuperuserFactory
from apps.books.tests.factories import AuthorFactory, GenreFactory, BookFactory
from apps.carts.tests.factories import CartFactory, CartItemFactory
from apps.orders.tests.factories import OrderFactory, OrderItemFactory


@pytest.fixture
def auth_user_model():
    """
    Fixture to provide an User model.
    :return: User model
    """

    yield get_user_model()


@pytest.fixture
def user(auth_user_model):
    """
    Fixture to provide an User.
    :return: User model
    """
    yield auth_user_model.objects.create_user_with_cart(
        username="testuser",
        password="testpassword",
        email="testuser@example.com",
    )


@pytest.fixture
def superuser(auth_user_model):
    """
    Fixture to provide an Superuser.
    :return: User model
    """
    yield auth_user_model.objects.create_superuser_with_cart(
        username="testsuperuser",
        password="testpassword",
        email="testsuperuser@example.com",
    )


@pytest.fixture
def user_factory():
    """
    Fixture to provide a UserFactory.
    :return: UserFactory
    """
    yield UserFactory


@pytest.fixture
def superuser_factory():
    """
    Fixture to provide a SuperuserFactory.
    :return: SuperuserFactory
    """
    yield SuperuserFactory


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
def author_model():
    """
    Fixture to provide an Author model.
    :return: Author model
    """
    yield Author


@pytest.fixture
def genre_model():
    """
    Fixture to provide an Genre model.
    :return: Genre model
    """
    yield Genre


@pytest.fixture
def book_model():
    """
    Fixture to provide an Book model.
    :return: Book model
    """
    yield Book


@pytest.fixture
def author_data():
    """
    Fixture to provide Author data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=AuthorFactory)


@pytest.fixture
def genre_data():
    """
    Fixture to provide Genre data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=GenreFactory)


@pytest.fixture
def book_data():
    """
    Fixture to provide Book data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=BookFactory)


@pytest.fixture
def author():
    """
    Fixture to provide Author.
    :return: Author
    """
    return AuthorFactory()


@pytest.fixture
def genre():
    """
    Fixture to provide Genre.
    :return: Genre
    """
    return GenreFactory()


@pytest.fixture
def book():
    """
    Fixture to provide Book.
    :return: Book
    """
    return BookFactory()


@pytest.fixture
def author_factory():
    """
    Fixture to provide AuthorFactory.
    :return: AuthorFactory
    """
    return AuthorFactory


@pytest.fixture
def genre_factory():
    """
    Fixture to provide GenreFactory.
    :return: GenreFactory
    """
    return GenreFactory


@pytest.fixture
def book_factory():
    """
    Fixture to provide BookFactory.
    :return: BookFactory
    """
    return BookFactory


@pytest.fixture
def temp_image_file():
    """
    Fixture to provide temporary image file.
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
def cart_model():
    """
    Fixture to provide an Cart model.
    :return: Cart model
    """
    yield Cart


@pytest.fixture
def cart_item_model():
    """
    Fixture to provide an CartItem model.
    :return: CartItem model
    """
    yield CartItem


@pytest.fixture
def cart_data():
    """
    Fixture to provide Cart data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=CartFactory)


@pytest.fixture
def cart_item_data():
    """
    Fixture to provide CartItem data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=CartItemFactory)


@pytest.fixture
def cart():
    """
    Fixture to provide Cart.
    :return: Cart
    """
    yield CartFactory()


@pytest.fixture
def cart_item():
    """
    Fixture to provide CartItemFactory.
    :return: CartItemFactory
    """
    yield CartItemFactory()


@pytest.fixture
def cart_factory():
    """
    Fixture to provide CartFactory.
    :return: CartFactory
    """
    return CartFactory


@pytest.fixture
def cart_item_factory():
    """
    Fixture to provide CartItemFactory.
    :return: CartItemFactory
    """
    return CartItemFactory


@pytest.fixture
def order_model():
    """
    Fixture to provide an Order model.
    :return: Order model
    """
    yield Order


@pytest.fixture
def order_item_model():
    """
    Fixture to provide an OrderItem model.
    :return: OrderItem model
    """
    yield OrderItem


@pytest.fixture
def order_data():
    """
    Fixture to provide Order data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=OrderFactory)


@pytest.fixture
def order_item_data():
    """
    Fixture to provide OrderItem data.
    :return: dict
    """
    return factory.build(dict, FACTORY_CLASS=OrderItemFactory)


@pytest.fixture
def order():
    """
    Fixture to provide Order.
    :return: Order
    """
    return OrderFactory()


@pytest.fixture
def order_item():
    """
    Fixture to provide OrderItem.
    :return: OrderItem
    """
    return OrderItemFactory()


@pytest.fixture
def order_factory():
    """
    Fixture to provide OrderFactory.
    :return: OrderFactory
    """
    return OrderFactory


@pytest.fixture
def order_item_factory():
    """
    Fixture to provide OrderItemFactory.
    :return: OrderItemFactory
    """
    return OrderItemFactory
