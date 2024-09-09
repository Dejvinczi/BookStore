from django.utils.translation import gettext as _
from rest_framework import serializers
from apps.books.serializers import BookListSerializer
from .models import Cart, CartItem


class BaseCartItemSerializer(serializers.ModelSerializer):
    """Base serializer for the CartItem model."""

    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=20,
        decimal_places=2,
    )

    class Meta:
        model = CartItem
        fields = "__all__"

    def validate_quantity(self, value):
        """Validation of quantity."""
        if value <= 0:
            raise serializers.ValidationError(
                {"quantity": _("Quantity must be a positive value.")}
            )
        return value


class CartItemListSerializer(BaseCartItemSerializer):
    """Serializer for listing the CartItem model isntances."""

    book = BookListSerializer(read_only=True)

    class Meta(BaseCartItemSerializer.Meta):
        fields = ("id", "book", "quantity", "total_price")
        read_only_fields = fields


class CartItemCreateSerializer(BaseCartItemSerializer):
    """Serializer for the creation of the CartItem model."""

    class Meta(BaseCartItemSerializer.Meta):
        fields = ("book", "quantity")
        extra_kwargs = {"quantity": {"read_only": True}}


class CartItemUpdateSerializer(BaseCartItemSerializer):
    """Serializer for the update of the CartItem model."""

    class Meta(BaseCartItemSerializer.Meta):
        fields = ("quantity",)


class BaseCartSerializer(serializers.ModelSerializer):
    """Serializer for the Cart model."""

    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=20,
        decimal_places=2,
    )

    class Meta:
        model = Cart
        fields = "__all__"


class CartRetrieveSerializer(BaseCartSerializer):
    """Serializer for the retrieve single Cart model instance."""

    items = CartItemListSerializer(many=True, read_only=True)

    class Meta(BaseCartSerializer.Meta):
        fields = ("items", "total_price")
        read_only_fields = fields
