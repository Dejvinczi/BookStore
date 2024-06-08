import pytest
import factory
from pytest_factoryboy import register
from .factories import AuthorFactory, GenreFactory, BookFactory


@pytest.fixture
def author_data():
    return factory.build(dict, FACTORY_CLASS=AuthorFactory)


@pytest.fixture
def genre_data():
    return factory.build(dict, FACTORY_CLASS=GenreFactory)


@pytest.fixture
def book_data():
    return factory.build(dict, FACTORY_CLASS=BookFactory)


register(AuthorFactory)
register(GenreFactory)
register(BookFactory)


@pytest.fixture
def author_factory():
    return AuthorFactory


@pytest.fixture
def genre_factory():
    return GenreFactory


@pytest.fixture
def book_factory():
    return BookFactory
