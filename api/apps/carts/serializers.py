from django.utils.translation import gettext as _
from rest_framework import serializers
from apps.books.serializers import BookListSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """Base serializer for the CartItem model."""

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


class CartItemListSerializer(CartItemSerializer):
    """Serializer for listing the CartItem model isntances."""

    book = BookListSerializer(read_only=True)

    class Meta(CartItemSerializer.Meta):
        model = CartItem
        fields = ("id", "book", "quantity")


class CartItemCreateSerializer(CartItemSerializer):
    """Serializer for the creation of the CartItem model."""

    class Meta(CartItemSerializer.Meta):
        fields = ("book", "quantity")
        extra_kwargs = {"quantity": {"read_only": True}}


class CartItemUpdateSerializer(CartItemSerializer):
    """Serializer for the update of the CartItem model."""

    class Meta(CartItemSerializer.Meta):
        fields = ("quantity",)


class CartSerializer(serializers.ModelSerializer):
    """Serializer for the Cart model."""

    class Meta:
        model = Cart
        fields = "__all__"


class CartRetrieveSerializer(CartSerializer):
    """Serializer for the retrieve single Cart model instance."""

    items = CartItemListSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        read_only=True,
        max_digits=20,
        decimal_places=2,
    )

    class Meta(CartSerializer.Meta):
        fields = ("items", "total_price")
