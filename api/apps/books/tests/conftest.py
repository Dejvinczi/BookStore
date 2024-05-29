import pytest
from ..models import Author, Genre


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
