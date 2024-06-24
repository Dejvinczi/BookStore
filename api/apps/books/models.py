from django.db import models
from django.core.validators import MinValueValidator
from apps.core.models import TimeStampedModel
from apps.core.validators import date_cannot_be_in_future
from .helpers import book_image_upload_to_path


class Author(TimeStampedModel):
    """Author model in the system."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(validators=[date_cannot_be_in_future])

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
    publication_date = models.DateField(validators=[date_cannot_be_in_future])
    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    image = models.ImageField(
        upload_to=book_image_upload_to_path,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title} ({self.publication_date})"
