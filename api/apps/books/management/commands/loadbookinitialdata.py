import json
import os
from django.core.files import File
from decimal import Decimal
from django.core.management.base import BaseCommand
from apps.books.models import Author, Genre, Book
from typing import Dict, List


class Command(BaseCommand):
    help = "Load initial books data with images"

    def _group_data(self, data: List[Dict]) -> Dict[str, List[Dict]]:
        grouped_data = {
            "genre": [],
            "author": [],
            "book": [],
        }

        for item in data:
            model_type = item["model"].lower().split(".")[-1]
            if model_type in grouped_data:
                grouped_data[model_type].append(item)

        return grouped_data

    def _create_genres(self, genre_data: List[Dict]) -> Dict[int, Genre]:
        self.stdout.write("Creating genres...")
        genres = {}

        for item in genre_data:
            genre = Genre.objects.create(
                id=item["pk"],
                name=item["fields"]["name"],
                created_at=item["fields"]["created_at"],
                updated_at=item["fields"]["updated_at"],
            )
            genres[item["pk"]] = genre
            self.stdout.write(f"Created genre: {genre.name}")

        return genres

    def _create_authors(self, author_data: List[Dict]) -> Dict[int, Author]:
        self.stdout.write("Creating authors...")
        authors = {}

        for item in author_data:
            author = Author.objects.create(
                id=item["pk"],
                first_name=item["fields"]["first_name"],
                last_name=item["fields"]["last_name"],
                date_of_birth=item["fields"]["date_of_birth"],
                created_at=item["fields"]["created_at"],
                updated_at=item["fields"]["updated_at"],
            )
            authors[item["pk"]] = author
            self.stdout.write(f"Created author: {author.first_name} {author.last_name}")

        return authors

    def _create_books(
        self,
        book_data: List[Dict],
        authors: Dict[int, Author],
        genres: Dict[int, Genre],
        app_dir: str,
    ) -> None:
        self.stdout.write("Creating books...")

        for item in book_data:
            book = Book.objects.create(
                id=item["pk"],
                title=item["fields"]["title"],
                description=item["fields"]["description"],
                publication_date=item["fields"]["publication_date"],
                price=Decimal(item["fields"]["price"]),
                created_at=item["fields"]["created_at"],
                updated_at=item["fields"]["updated_at"],
            )

            book.authors.set(
                [authors[author_id] for author_id in item["fields"]["authors"]]
            )
            book.genres.set([genres[genre_id] for genre_id in item["fields"]["genres"]])

            image_path = os.path.join(
                app_dir, "fixtures", "images", f"book{item['pk']}.jpg"
            )
            if os.path.exists(image_path):
                with open(image_path, "rb") as image_file:
                    book.image.save(
                        f"book{item['pk']}.jpg", File(image_file), save=True
                    )

            self.stdout.write(f"Created book: {book.title}")

    def handle(self, *args, **options):
        app_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        json_file_path = os.path.join(app_dir, "fixtures", "initial_data.json")

        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        grouped_data = self._group_data(data)

        self.stdout.write("Clearing existing data...")
        Book.objects.all().delete()
        Author.objects.all().delete()
        Genre.objects.all().delete()

        genres = self._create_genres(grouped_data["genre"])
        authors = self._create_authors(grouped_data["author"])
        self._create_books(grouped_data["book"], authors, genres, app_dir)

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                    Summary:
                    - Created {Genre.objects.count()} genres
                    - Created {Author.objects.count()} authors
                    - Created {Book.objects.count()} books with images
                """
            )
        )
