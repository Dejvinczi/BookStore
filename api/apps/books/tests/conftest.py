import os
import pytest
import factory
import tempfile
from PIL import Image
from pytest_factoryboy import register
from .factories import AuthorFactory, GenreFactory, BookFactory


@pytest.fixture
def author_data():
    """Fixture for author data."""
    return factory.build(dict, FACTORY_CLASS=AuthorFactory)


@pytest.fixture
def genre_data():
    """Fixture for genre data."""
    return factory.build(dict, FACTORY_CLASS=GenreFactory)


@pytest.fixture
def book_data():
    """Fixture for book data."""
    return factory.build(dict, FACTORY_CLASS=BookFactory)


register(AuthorFactory)
register(GenreFactory)
register(BookFactory)


@pytest.fixture
def author_factory():
    """Fixture for author factory."""
    return AuthorFactory


@pytest.fixture
def genre_factory():
    """Fixture for genre factory."""
    return GenreFactory


@pytest.fixture
def book_factory():
    """Fixture for book factory."""
    return BookFactory


@pytest.fixture
def temp_image_file():
    try:
        temp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)

        image = Image.new("RGB", (100, 100), color="red")
        image.save(temp, format="JPEG")

        temp.close()

        yield temp.name
    finally:
        try:
            os.remove(temp.name)
        except (AttributeError, FileNotFoundError):
            pass
