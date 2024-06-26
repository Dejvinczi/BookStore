from collections import OrderedDict
from rest_framework import serializers


class NestedPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def __init__(self, serializer_class, **kwargs):
        """
        On read display a complete nested representation of the object(s)
        On write only require the PK (not an entire object) as value
        """
        self.serializer_class = serializer_class
        super().__init__(**kwargs)

    def to_representation(self, obj):
        return self.serializer_class(obj, context=self.context).data

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict([(item.pk, self.display_value(item)) for item in queryset])

    def use_pk_only_optimization(self):
        return False
