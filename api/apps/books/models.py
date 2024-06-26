from django.db import models
from apps.core.models import TimeStampedModel
from .helpers import book_image_upload_to_path


class Author(TimeStampedModel):
    """Author model in the system."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(TimeStampedModel):
    """Genre model in the system."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    """Book model in the system."""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    image = models.ImageField(
        upload_to=book_image_upload_to_path,
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.publication_date})"
