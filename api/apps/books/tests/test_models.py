import pytest
from ..models import Author, Genre


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


@pytest.mark.django_db
class TestGenreModel:
    """Tests for the Genre model in the system."""

    @pytest.fixture
    def genre_data(self):
        return {"name": "Test Genre"}

    @pytest.fixture
    def genre(self, genre_data):
        return Genre.objects.create(**genre_data)

    def test_create_genre(self, genre_data):
        """Test that the Genre model can be created."""
        genre = Genre.objects.create(**genre_data)
        genres = Genre.objects.all()

        assert genres.count() == 1
        assert genres.first() == genre

    def test_str(self, genre):
        """Test that the Genre model returns the correct string representation."""
        assert genre.name == str(genre)
