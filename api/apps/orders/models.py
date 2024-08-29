from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel
from .helpers import generate_order_number


User = settings.AUTH_USER_MODEL


class Order(TimeStampedModel):
    """Order model in the system."""

    class StatusChoices(models.TextChoices):
        """Order status choices."""

        NEW = "new"
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"
        CANCELED = "canceled"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    no = models.SlugField(
        max_length=32,
        unique=True,
        editable=False,
        default=generate_order_number,
    )
    status = models.CharField(
        max_length=255,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )

    def __str__(self):
        return f"Order {self.no}"

    @property
    def total_price(self):
        value = sum(item.total_price for item in self.items.all())
        return value


class OrderItem(TimeStampedModel):
    """Order item model in the system."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Book {self.book.title} ({self.quantity})"

    @property
    def total_price(self):
        value = self.price * self.quantity
        return value
