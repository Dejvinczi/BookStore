from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.utils import Direction
from .serializers import NestedPrimaryKeyRelatedField


class NestedPrimaryKeyRelatedFieldExtension(OpenApiSerializerFieldExtension):
    # Ensure annotations use different read/write serializers when using NestedPrimaryKeyRelatedField
    target_class = NestedPrimaryKeyRelatedField

    def map_serializer_field(self, auto_schema, direction: Direction):
        if direction == "response":
            # Target is NestedPrimaryKeyRelatedField instance.
            # build a component from the serializer and return a reference to that component
            component = auto_schema.resolve_serializer(
                self.target.serializer_class, direction
            )
            return component.ref if component else None
        else:
            return auto_schema._map_serializer_field(
                self.target, direction, bypass_extensions=True
            )
