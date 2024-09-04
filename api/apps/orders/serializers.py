from django.utils.translation import gettext as _
from rest_framework import serializers
from apps.books.serializers import BookListSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model."""

    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate_quantity(self, value):
        """Validation of quantity."""
        if value <= 0:
            raise serializers.ValidationError(
                {"quantity": _("Quantity must be a positive value.")}
            )
        return value

    def validate_price(self, value):
        """Validation of price."""
        if value <= 0:
            raise serializers.ValidationError(
                {"price": _("Price must be a positive value.")}
            )
        return value


class OrderItemListSerializer(OrderItemSerializer):
    """Serializer for listing the OrderItem model isntances."""

    book = BookListSerializer(read_only=True)

    class Meta(OrderItemSerializer.Meta):
        fields = ("id", "book", "quantity", "price")


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model."""

    status = serializers.CharField(read_only=True)
    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderListSerializer(OrderSerializer):
    """Serializer for listing the Order model."""

    class Meta(OrderSerializer.Meta):
        fields = ("id", "no", "address", "status", "total_price")


class OrderDetailSerializer(OrderSerializer):
    """Serializer for detail the Order model."""

    items = OrderItemListSerializer(many=True, read_only=True)

    class Meta(OrderSerializer.Meta):
        fields = ("id", "no", "address", "items", "status", "total_price")
