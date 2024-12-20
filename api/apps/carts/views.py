from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import (
    BaseCartItemSerializer,
    CartRetrieveSerializer,
    CartItemCreateSerializer,
    CartItemUpdateSerializer,
)


class CartAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """View for the user cart."""

    queryset = Cart.objects.prefetch_related(
        Prefetch("items", queryset=CartItem.objects.select_related("book")),
        "items__book__authors",
        "items__book__genres",
    ).all()
    serializer_class = CartRetrieveSerializer

    def get_object(self):
        """Get current user cart."""
        obj = get_object_or_404(self.queryset, user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

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

    queryset = CartItem.objects.all()
    serializer_class = BaseCartItemSerializer
    action_serializer_classes = {
        "create": CartItemCreateSerializer,
        "update": CartItemUpdateSerializer,
        "partial_update": CartItemUpdateSerializer,
    }

    def get_serializer_class(self):
        """Get serializer class based on action."""
        serializer_class = self.action_serializer_classes.get(
            self.action, self.serializer_class
        )
        return serializer_class

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
