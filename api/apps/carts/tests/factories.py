import factory
from ..models import Cart, CartItem


class CartFactory(factory.django.DjangoModelFactory):
    """Factory for Cart model."""

    class Meta:
        model = Cart

    user = factory.SubFactory("apps.accounts.tests.factories.UserFactory")


class CartItemFactory(factory.django.DjangoModelFactory):
    """Factory for CartItem model."""

    class Meta:
        model = CartItem

    cart = factory.SubFactory("apps.carts.tests.factories.CartFactory")
    book = factory.SubFactory("apps.books.tests.factories.BookFactory")
    quantity = factory.Faker("random_int", min=1, max=10)
