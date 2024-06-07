import pytest
from django.core import exceptions as d_exceptions
from django.utils import timezone
from ..validators import date_cannot_be_in_future


def test_date_cannot_be_in_future_error():
    """Test that date cannot be in the future"""
    with pytest.raises(d_exceptions.ValidationError):
        next_week = timezone.now().date() + timezone.timedelta(days=7)
        date_cannot_be_in_future(next_week)


def test_date_cannot_be_in_future_success():
    """Test that date can be in the future"""
    next_week = timezone.now().date()
    validated_value = date_cannot_be_in_future(next_week)
    assert next_week == validated_value
