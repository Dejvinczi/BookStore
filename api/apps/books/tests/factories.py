import factory
from django.utils import timezone
from ..models import Author, Genre, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_of_birth = factory.Faker("date", end_datetime=timezone.now().date())


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: f"Genre {n}")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f"Book {n}")
    description = factory.Faker("paragraph", nb_sentences=3)
    publication_date = factory.Faker("date", end_datetime=timezone.now().date())
    price = factory.Faker("pydecimal", left_digits=6, right_digits=2, positive=True)
