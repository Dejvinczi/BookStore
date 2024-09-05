from unittest.mock import Mock
from ..helpers import book_image_upload_to_path


def test_book_image_upload_to_path():
    """Test that the book image upload path is correct."""
    mock_instance = Mock()
    mock_instance.id = 5
    assert book_image_upload_to_path(mock_instance, "test.png") == "books/5/test.png"
