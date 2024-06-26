from django.db import models
from apps.core.models import TimeStampedModel


class Cart(TimeStampedModel):
    """Shop cart model in the system."""

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(TimeStampedModel):
    """Shop cart item model in the system."""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
