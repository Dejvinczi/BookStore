from ..pagination import CustomLimitOffsetPagination


class TestCustomLimitOffsetPagination:
    """Test CustomLimitOffsetPagination class."""

    def test_default_limit(self):
        """Test default_limit attribute."""
        custom_limit_offset_pagination = CustomLimitOffsetPagination()
        assert custom_limit_offset_pagination.default_limit == 5
