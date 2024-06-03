import factory
from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Author, Genre, Book


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    date_of_birth = Faker("date_of_birth")


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = Faker("word")


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = Faker("sentence", nb_words=4)
    description = Faker("paragraph", nb_sentences=3)
    publication_date = Faker("date")
