from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from .models import Order
from .serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    OrderItemSerializer,
)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """View for orders."""

    queryset = Order.objects.prefetch_related("items", "items__book").all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        """Get current user orders."""
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Get serializer class based on action."""
        if self.action == "list":
            return OrderListSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Save the new order with the current user."""
        return serializer.save(user=self.request.user)

    @transaction.atomic()
    def create(self, request):
        """Create an order based on the items in the user's cart."""
        cart = request.user.cart
        cart_items = cart.items.prefetch_related("book").all()
        if not cart_items.exists():
            return Response(
                {"detail": _("Cart is empty")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_serializer = self.get_serializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = self.perform_create(order_serializer)

        order_id = order.id
        order_items = []
        for item in cart_items:
            order_items.append(
                {
                    "order": order_id,
                    "book": item.book.id,
                    "quantity": item.quantity,
                    "price": item.book.price,
                }
            )
        order_item_serializer = OrderItemSerializer(data=order_items, many=True)
        order_item_serializer.is_valid(raise_exception=True)
        order_item_serializer.save()

        cart_items.delete()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
