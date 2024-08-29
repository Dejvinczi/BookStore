import pytest
from ..models import Order, OrderItem


@pytest.mark.django_db
class TestOrderModel:
    """Tests for the Order model in the system."""

    def test_create_order(self, user):
        """Test that the Order model can be created."""
        order = Order.objects.create(user=user)
        assert order.id is not None
        assert order.user == user
        assert order.status == Order.StatusChoices.NEW
        assert order.total_price == 0

    def test_order_statuses(self):
        """Test that the Order statuses are correct."""
        assert Order.StatusChoices.NEW == "new"
        assert Order.StatusChoices.IN_PROGRESS == "in_progress"
        assert Order.StatusChoices.COMPLETED == "completed"
        assert Order.StatusChoices.CANCELED == "canceled"

    def test_str(self, user):
        """Test that the Order model returns the correct string representation."""
        order = Order.objects.create(user=user)
        assert str(order) == f"Order {order.no}"

    def test_total_price(self, user, order_item_factory):
        """Test that the total price is calculated correctly."""
        order = Order.objects.create(user=user)
        order_items = order_item_factory.create_batch(2, order=order)
        assert order.total_price == sum(
            order_item.total_price for order_item in order_items
        )


@pytest.mark.django_db
class TestOrderItemModel:
    """Tests for the OrderItem model in the system."""

    def test_create_order_item(self, order, book):
        """Test that the OrderItem model can be created."""
        order_item_data = {"order": order, "book": book, "price": 20}
        order_item = OrderItem.objects.create(**order_item_data)
        assert order_item.id is not None
        assert order_item.order == order
        assert order_item.quantity == 1
        assert order_item.price == 20
        assert order_item.total_price == 20

    def test_str(self, order, book):
        """Test that the OrderItem model returns the correct string representation."""
        order_item_data = {"order": order, "book": book, "price": 20}
        order_item = OrderItem.objects.create(**order_item_data)
        excepted_str = f"Book {order_item.book.title} ({order_item.quantity})"
        assert str(order_item) == excepted_str

    def test_total_price(self, order, book):
        """Test that the total price is calculated correctly."""
        order_item = OrderItem.objects.create(
            order=order,
            book=book,
            price=100,
            quantity=3,
        )
        assert order_item.total_price == order_item.price * order_item.quantity
