import pytest
from ..models import Author, Genre, Book


@pytest.fixture
def author_data():
    """
    Fixture to provide author data
    :return: dict
    """
    return {
        "first_name": "testfirstname",
        "last_name": "testlastname",
        "date_of_birth": "1990-01-01",
    }


@pytest.fixture
def author(author_data):
    """
    Fixture to provide an author instance
    :param author_data: dict
    :return: Author
    """
    return Author.objects.create(**author_data)


@pytest.fixture
def genre_data():
    """
    Fixture to provide genre data
    :return: dict
    """
    return {"name": "Test Genre"}


@pytest.fixture
def genre(genre_data):
    """
    Fixture to provide a genre instance
    :param genre_data: dict
    :return: Genre
    """
    return Genre.objects.create(**genre_data)


@pytest.fixture
def book_data():
    """
    Fixture to provide book data
    :param author: Author
    :param genre: Genre
    :return: dict
    """
    return {
        "title": "Test Book",
        "description": "Test Description",
        "publication_date": "2020-01-01",
    }


@pytest.fixture
def book(book_data):
    """
    Fixture to provide a book instance
    :param book_data: dict
    :return: Book
    """
    return Book.objects.create(**book_data)
