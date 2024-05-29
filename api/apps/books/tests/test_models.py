import pytest
from ..models import Author


@pytest.mark.django_db
class TestAuthorModel:
    """Tests for the Author model in the system."""

    @pytest.fixture
    def author_data(self):
        return {
            "first_name": "testfirstname",
            "last_name": "testlastname",
            "date_of_birth": "1990-01-01",
        }

    @pytest.fixture
    def author(self, author_data):
        return Author.objects.create(**author_data)

    def test_create_author(self, author_data):
        """Test that the Author model can be created."""
        author = Author.objects.create(**author_data)
        authors = Author.objects.all()

        assert authors.count() == 1
        assert authors.first() == author

    def test_str(self, author):
        """Test that the Author model returns the correct string representation."""
        assert f"{author.first_name} {author.last_name}" == str(author)
