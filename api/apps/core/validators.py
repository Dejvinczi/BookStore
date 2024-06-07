from django.core import exceptions as d_exceptions
from django.utils.translation import gettext as _
from django.utils import timezone


def date_cannot_be_in_future(value):
    if value > timezone.now().date():
        raise d_exceptions.ValidationError(_("Date cannot be in the future."))
    return value
