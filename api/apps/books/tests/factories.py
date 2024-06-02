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

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)
        else:
            authors = AuthorFactory.create_batch(3)
            self.authors.set(authors)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genres.add(genre)
        else:
            genres = GenreFactory.create_batch(2)
            self.genres.set(genres)
