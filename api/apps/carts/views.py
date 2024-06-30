from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from .models import CartItem
from .serializers import (
    CartRetrieveSerializer,
    CartItemCreateSerializer,
    CartItemUpdateSerializer,
)


class CartRetrieveAPIView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    """View for the user cart."""

    serializer_class = CartRetrieveSerializer

    def get_object(self):
        """Get current user cart."""
        return self.request.user.cart

    def get(self, request, *args, **kwargs):
        """Retrieve user cart."""
        return self.retrieve(request, *args, **kwargs)


class CartItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Viewset for the CartItem model."""

    def get_queryset(self):
        """Get current user cart items."""
        user_cart = self.request.user.cart
        queryset = CartItem.objects.filter(cart=user_cart)
        return queryset

    def get_serializer_class(self):
        """Get serializer class based on action."""
        if self.action == "create":
            return CartItemCreateSerializer
        if self.action in ["partial_update", "update"]:
            return CartItemUpdateSerializer

    def perform_create(self, serializer):
        """Create a new cart item for the current user cart."""
        serializer.save(cart=self.request.user.cart)

    def create(self, request, *args, **kwargs):
        """Create a new cart item or update quantity if it exists."""
        try:
            book_id = request.data.get("book")
            cart_item = self.get_queryset().get(book_id=book_id)
            cart_item.quantity += 1
            cart_item.save()
            serializer = self.get_serializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return super().create(request, *args, **kwargs)
