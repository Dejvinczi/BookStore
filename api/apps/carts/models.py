from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel


class Cart(TimeStampedModel):
    """Shop cart model in the system."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart",
    )

    def __str__(self):
        return f"{self.user.username}'s cart"

    @property
    def total_price(self):
        value = sum(item.total_price for item in self.items.all())
        return value


class CartItem(TimeStampedModel):
    """Shop cart item model in the system."""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.book.price * self.quantity
