from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from .tasks import send_order_change_status_email
from .models import Order
from .serializers import (
    BaseOrderSerializer,
    OrderListSerializer,
    OrderRetrieveSerializer,
    OrderCreateSerializer,
    BaseOrderItemSerializer,
)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """View for orders."""

    queryset = Order.objects.prefetch_related("items", "items__book").all()
    serializer_class = BaseOrderSerializer
    action_serializer_classes = {
        "list": OrderListSerializer,
        "retrieve": OrderRetrieveSerializer,
        "create": OrderCreateSerializer,
    }

    def get_queryset(self):
        """Get current user orders."""
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Get serializer class based on action."""
        serializer_class = self.action_serializer_classes.get(
            self.action, self.serializer_class
        )
        return serializer_class

    def perform_create(self, serializer):
        """Save the new order with the current user."""
        return serializer.save(user=self.request.user)

    def create(self, request):
        """Create an order based on the items in the user's cart."""
        cart = request.user.cart
        cart_items = cart.items.prefetch_related("book").all()
        if not cart_items.exists():
            return Response(
                {"detail": _("Cart is empty")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
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
            order_item_serializer = BaseOrderItemSerializer(data=order_items, many=True)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save()

            cart_items.delete()
            transaction.on_commit(
                lambda: send_order_change_status_email.delay(order_id)
            )

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
