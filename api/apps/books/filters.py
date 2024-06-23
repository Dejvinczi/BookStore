from django_filters import rest_framework as drf_filters
from .models import Author, Genre, Book


class AuthorFilter(drf_filters.FilterSet):
    """Filter class for the Author model."""

    first_name = drf_filters.CharFilter(
        field_name="first_name",
        label="First Name",
        lookup_expr="icontains",
        help_text="Filter by first name (case insensitive).",
    )
    last_name = drf_filters.CharFilter(
        field_name="last_name",
        label="Last Name",
        lookup_expr="icontains",
        help_text="Filter by last name (case insensitive).",
    )
    date_of_birth = drf_filters.DateFromToRangeFilter(
        field_name="date_of_birth",
        label="Date of Birth range",
        help_text="Filter by date of birth (range). Format: YYYY-MM-DD",
    )
    ordering = drf_filters.OrderingFilter(
        fields=["first_name", "last_name", "date_of_birth"],
        field_labels={
            "first_name": "First Name",
            "last_name": "Last Name",
            "date_of_birth": "Date of Birth",
        },
        help_text="Order by field. Prefix with '-' for descending order.",
    )

    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth"]


class GenreFilter(drf_filters.FilterSet):
    """Filter class for the Genre model."""

    name = drf_filters.CharFilter(
        field_name="name",
        label="Name",
        lookup_expr="icontains",
        help_text="Filter by name (case insensitive).",
    )
    ordering = drf_filters.OrderingFilter(
        fields=["name"],
        field_labels={"name": "Name"},
        help_text="Order by field. Prefix with '-' for descending order.",
    )

    class Meta:
        model = Genre
        fields = ["name"]


class BookFilter(drf_filters.FilterSet):
    """Filter class for the Book model."""

    title = drf_filters.CharFilter(
        field_name="title",
        label="Title",
        lookup_expr="icontains",
        help_text="Filter by title (case insensitive).",
    )
    publication_date = drf_filters.DateFromToRangeFilter(
        field_name="publication_date",
        label="Date of publication",
        help_text="Filter by date of birth (range). Format: YYYY-MM-DD",
    )
    ordering = drf_filters.OrderingFilter(
        fields=["title", "publication_date"],
        field_labels={"title": "Title", "publication_date": "Date of publication"},
        help_text="Order by field. Prefix with '-' for descending order.",
    )

    class Meta:
        model = Book
        fields = ["title", "publication_date"]
