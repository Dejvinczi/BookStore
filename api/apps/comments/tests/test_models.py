import pytest
from apps.books.tests.factories import BookFactory
from ..models import Comment


@pytest.mark.django_db
class TestCommentModel:
    """Tests for the Comment model in the system."""

    def test_create_comment(self, user):
        """Test that the Comment model can be created."""
        book = BookFactory()
        comment_data = {
            "text": "Test Comment text",
            "book": book,
            "user": user,
        }
        comment = Comment.objects.create(**comment_data)

        assert comment.text == comment_data["text"]
        assert comment.book == comment_data["book"]
        assert comment.user == comment_data["user"]
        assert comment.created_at is not None
        assert comment.updated_at is not None
