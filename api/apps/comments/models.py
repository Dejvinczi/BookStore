from django.db import models


class Comment(models.Model):
    """Comment model in the system."""

    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
