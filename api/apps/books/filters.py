from django_filters import rest_framework as drf_filters
from .models import Author, Genre


class AuthorFilter(drf_filters.FilterSet):
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
