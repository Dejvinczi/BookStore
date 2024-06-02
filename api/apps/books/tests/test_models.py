import pytest
from ..models import Author, Genre, Book


@pytest.mark.django_db
class TestAuthorModel:
    """Tests for the Author model in the system."""

    def test_create_author(self, author_data):
        """Test that the Author model can be created."""
        author = Author.objects.create(**author_data)
        authors = Author.objects.all()

        assert authors.count() == 1
        assert authors.first() == author

    def test_str(self, author):
        """Test that the Author model returns the correct string representation."""
        excepted_str = f"{author.first_name} {author.last_name}"
        assert str(author) == excepted_str


@pytest.mark.django_db
class TestGenreModel:
    """Tests for the Genre model in the system."""

    def test_create_genre(self, genre_data):
        """Test that the Genre model can be created."""
        genre = Genre.objects.create(**genre_data)
        genres = Genre.objects.all()

        assert genres.count() == 1
        assert genres.first() == genre

    def test_str(self, genre):
        """Test that the Genre model returns the correct string representation."""
        excepted_str = genre.name
        assert str(genre) == excepted_str


@pytest.mark.django_db
class TestBookModel:
    """Tests for the Book model in the system."""

    def test_create_book(self, book_data):
        """Test that the Book model can be created."""
        book = Book.objects.create(**book_data)
        books = Book.objects.all()

        assert books.count() == 1
        assert books.first() == book

    def test_str(self, book):
        """Test that the Book model returns the correct string representation."""
        excepted_str = f"{book.title} ({book.publication_date})"
        assert str(book) == excepted_str

    def test_assign_author(self, book, author):
        """Test that the Book model can be assigned an author."""
        book.authors.add(author)
        assert book.authors.first() == author

    def test_assign_genre(self, book, genre):
        """Test that the Book model can be assigned a genre."""
        book.genres.add(genre)
        assert book.genres.first() == genre

    def test_remove_author(self, book, author):
        """Test that the Book model can be removed from an author."""
        book.authors.add(author)
        assert book.authors.first() == author
        book.authors.remove(author)
        assert book.authors.count() == 0

    def test_remove_genre(self, book, genre):
        """Test that the Book model can be removed from a genre."""
        book.genres.add(genre)
        assert book.genres.first() == genre
        book.genres.remove(genre)
        assert book.genres.count() == 0
