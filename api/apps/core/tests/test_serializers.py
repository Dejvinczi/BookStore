import pytest
from collections import OrderedDict
from unittest.mock import Mock
from ..serializers import NestedPrimaryKeyRelatedField


@pytest.fixture
def mock_serializer_class():
    serializer_class = Mock()
    serializer_class.return_value.data = {"mocked_data": "mocked"}
    return serializer_class


class TestNestedPrimaryKeyRelatedField:
    def test_init(self, mock_serializer_class):
        nested_field = NestedPrimaryKeyRelatedField(
            serializer_class=mock_serializer_class,
            read_only=True,
        )
        assert nested_field.serializer_class == mock_serializer_class
        assert nested_field.read_only

    def test_to_representation(self, mock_serializer_class):
        obj = Mock(pk=1)
        nested_field = NestedPrimaryKeyRelatedField(
            serializer_class=mock_serializer_class,
            read_only=True,
        )
        result = nested_field.to_representation(obj)
        assert result == {"mocked_data": "mocked"}

    def test_get_choices(self, mock_serializer_class):
        queryset = [Mock(pk=1), Mock(pk=2), Mock(pk=3)]
        nested_field = NestedPrimaryKeyRelatedField(
            serializer_class=mock_serializer_class,
            read_only=True,
        )
        nested_field.get_queryset = Mock(return_value=queryset)
        choices = nested_field.get_choices()
        assert choices == OrderedDict(
            [
                (queryset[0].pk, nested_field.display_value(queryset[0])),
                (queryset[1].pk, nested_field.display_value(queryset[1])),
                (queryset[2].pk, nested_field.display_value(queryset[2])),
            ]
        )

    def test_get_choices_with_cutoff(self, mock_serializer_class):
        queryset = [Mock(pk=1), Mock(pk=2), Mock(pk=3)]
        nested_field = NestedPrimaryKeyRelatedField(
            serializer_class=mock_serializer_class,
            read_only=True,
        )
        nested_field.get_queryset = Mock(return_value=queryset)
        choices = nested_field.get_choices(cutoff=2)
        assert choices == OrderedDict(
            [
                (queryset[0].pk, nested_field.display_value(queryset[0])),
                (queryset[1].pk, nested_field.display_value(queryset[1])),
            ]
        )

    def test_get_choices_without_queryset(self, mock_serializer_class):
        nested_field = NestedPrimaryKeyRelatedField(
            serializer_class=mock_serializer_class,
            read_only=True,
        )
        assert nested_field.get_choices() == OrderedDict()
