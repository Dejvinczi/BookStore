import pytest
from rest_framework import serializers
from ..serializers import OrderItemSerializer


@pytest.mark.django_db(transaction=True)
class TestOrderItemSerializer:
    """Test OrderItemSerializer."""

    @pytest.fixture(autouse=True)
    def setup_method(self, book, order):
        """Setup method."""
        self.serializer = OrderItemSerializer
        self.data = {
            "order": order.id,
            "book": book.id,
            "quantity": 1,
            "price": book.price,
        }

    def test_validate_quantity_success(self):
        """Test validate quantity success."""
        serializer = self.serializer(data=self.data)
        assert serializer.is_valid()

    def test_validate_price_success(self):
        """Test validate price success."""
        serializer = self.serializer(data=self.data)
        assert serializer.is_valid()

    def test_validate_non_positive_quantity_fail(self):
        """Test validate non positive quantity."""
        with pytest.raises(serializers.ValidationError):
            self.data["quantity"] = 0
            serializer = self.serializer(data=self.data)
            serializer.is_valid(raise_exception=True)

    def test_validate_non_positive_price_fail(self):
        """Test validate non positive price."""
        with pytest.raises(serializers.ValidationError):
            self.data["price"] = 0
            serializer = self.serializer(data=self.data)
            serializer.is_valid(raise_exception=True)
