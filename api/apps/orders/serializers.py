from django.utils.translation import gettext as _
from rest_framework import serializers
from apps.books.serializers import BookListSerializer
from .models import Order, OrderItem


class BaseOrderItemSerializer(serializers.ModelSerializer):
    """Base serializer for the OrderItem model."""

    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=10,
        decimal_places=2,
    )

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


class OrderItemListSerializer(BaseOrderItemSerializer):
    """Serializer for listing the OrderItem model isntances."""

    book = BookListSerializer(read_only=True)

    class Meta(BaseOrderItemSerializer.Meta):
        fields = ("id", "book", "quantity", "price")


class BaseOrderSerializer(serializers.ModelSerializer):
    """Base serializer for the Order model."""

    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "no": {"read_only": True},
            "status": {"read_only": True},
        }


class OrderListSerializer(BaseOrderSerializer):
    """Serializer for listing the Orders."""

    class Meta(BaseOrderSerializer.Meta):
        fields = ("id", "no", "address", "status", "total_price")


class OrderRetrieveSerializer(BaseOrderSerializer):
    """Serializer for retrieving the Order."""

    items = OrderItemListSerializer(many=True, read_only=True)

    class Meta(BaseOrderSerializer.Meta):
        fields = ("id", "no", "address", "items", "status", "total_price")


class OrderCreateSerializer(BaseOrderSerializer):
    """Serializer for creating the Orders."""

    class Meta(BaseOrderSerializer.Meta):
        fields = ("id", "no", "address", "total_price")
