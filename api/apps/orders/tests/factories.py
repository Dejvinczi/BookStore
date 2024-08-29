import factory
from ..models import Order, OrderItem


class OrderFactory(factory.django.DjangoModelFactory):
    """Factory for Order model."""

    class Meta:
        model = Order

    user = factory.SubFactory("apps.accounts.tests.factories.UserFactory")
    status = factory.Iterator(Order.StatusChoices.choices)


class OrderItemFactory(factory.django.DjangoModelFactory):
    """Factory for OrderItem model."""

    class Meta:
        model = OrderItem

    order = factory.SubFactory("apps.orders.tests.factories.OrderFactory")
    book = factory.SubFactory("apps.books.tests.factories.BookFactory")
    quantity = factory.Faker("random_int", min=1, max=10)
    price = factory.Faker("pydecimal", left_digits=6, right_digits=2, positive=True)
