import os
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestAuthorViewSet:
    """Tests for the AuthorViewSet."""

    AUTHOR_LIST_URL = reverse("books:author-list")

    def _get_book_detail_url(self, id):
        return reverse("books:author-detail", args=[id])

    def test_list_success(self, api_client):
        """Test that the list of authors can be retrieved."""
        response = api_client.get(self.AUTHOR_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated_success(self, api_client, author_factory):
        """Test that the list of authors can be retrieved with pagination."""
        author_factory.create_batch(5)
        response = api_client.get(self.AUTHOR_LIST_URL, {"limit": 1})
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_list_with_filter_first_name_success(self, api_client, author_factory):
        """Test that the list of authors can be filtered by first name."""
        author_factory.create_batch(5)
        filter_author = author_factory(first_name="Non-ExstiningName")

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"first_name": filter_author.first_name},
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert len(response.data["results"]) == 1

    def test_list_with_filter_last_name_success(self, api_client, author_factory):
        """Test that the list of authors can be filtered by last name."""
        authors = author_factory.create_batch(5)
        first_author = authors[0]
        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"last_name": first_author.last_name},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert len(response.data["results"]) == 1

    def test_list_with_filter_date_of_birth_success(self, api_client, author_factory):
        """Test that the list of authors can be filtered by date of birth."""
        authors = [
            author_factory.create(date_of_birth=f"2000-01-0{idx}")
            for idx in range(1, 6)
        ]
        first_author = authors[0]

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {
                "date_of_birth_after": first_author.date_of_birth,
                "date_of_birth_before": first_author.date_of_birth,
            },
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert len(response.data["results"]) == 1

    def test_list_with_ordering_by_first_name_success(self, api_client, author_factory):
        """Test that the list of authors can be ordered by first name."""
        authors = author_factory.create_batch(5)
        ordered_authors = sorted(authors, key=lambda author: author.first_name.lower())

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "first_name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["id"] == ordered_authors[0].id

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "-first_name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][-1]["id"] == ordered_authors[0].id

    def test_list_with_ordering_by_last_name_success(self, api_client, author_factory):
        """Test that the list of authors can be ordered by last name."""
        authors = author_factory.create_batch(5)
        ordered_authors = sorted(authors, key=lambda author: author.last_name.lower())

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "last_name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert [author["id"] for author in response.data["results"]] == [
            author.id for author in ordered_authors
        ]

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "-last_name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert [author["id"] for author in response.data["results"]] == [
            author.id for author in reversed(ordered_authors)
        ]

    def test_list_with_ordering_by_date_of_birth_success(
        self, api_client, author_factory
    ):
        """Test that the list of authors can be ordered by date of birth."""
        authors = author_factory.create_batch(5)
        ordered_authors = sorted(authors, key=lambda author: author.date_of_birth)

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "date_of_birth"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["id"] == ordered_authors[0].id

        response = api_client.get(
            f"{self.AUTHOR_LIST_URL}",
            {"ordering": "-date_of_birth"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][-1]["id"] == ordered_authors[0].id

    def test_retrieve_success(self, api_client, author):
        """Test that an author can be retrieved."""
        response = api_client.get(self._get_book_detail_url(author.id))
        assert response.status_code == status.HTTP_200_OK

    def test_create_not_as_admin_fail(self, auth_api_client):
        """Test that an author can't be created for users that are not admin."""
        response = auth_api_client.post(self.AUTHOR_LIST_URL, {})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_not_as_admin_fail(self, auth_api_client, author):
        """Test that an author can't be updated for users that are not admin."""
        response = auth_api_client.put(
            self._get_book_detail_url(author.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_part_update_not_as_admin_fail(self, auth_api_client, author):
        """Test that an author can't be partially updated for users that are not admin."""
        response = auth_api_client.patch(
            self._get_book_detail_url(author.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_not_as_admin_fail(self, auth_api_client, author):
        """Test that an author can't be deleted for users that are not admin."""
        response = auth_api_client.delete(self._get_book_detail_url(author.id))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_as_admin_success(self, admin_api_client):
        """Test that an author can be created for users that are admin."""
        payload = {
            "first_name": "Test",
            "last_name": "Author",
            "date_of_birth": "2000-01-01",
        }
        response = admin_api_client.post(self.AUTHOR_LIST_URL, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_as_admin_success(self, admin_api_client, author):
        """Test that an author can be updated for users that are admin."""
        payload = {
            "first_name": "Test",
            "last_name": "Author",
            "date_of_birth": "2000-01-01",
        }
        response = admin_api_client.put(
            self._get_book_detail_url(author.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_part_update_as_admin_success(self, admin_api_client, author):
        """Test that an author can be partially updated for users that are admin."""
        payload = {"first_name": "Test"}
        response = admin_api_client.patch(
            self._get_book_detail_url(author.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_delete_as_admin_success(self, admin_api_client, author):
        """Test that an author can be deleted for users that are admin."""
        response = admin_api_client.delete(self._get_book_detail_url(author.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class TestGenreViewSet:
    """Tests for the GenreViewSet."""

    GENRE_LIST_URL = reverse("books:genre-list")

    def _get_book_detail_url(self, id):
        return reverse("books:genre-detail", args=[id])

    def test_list_success(self, api_client):
        """Test that the list of genres can be retrieved."""
        response = api_client.get(self.GENRE_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated(self, api_client, genre_factory):
        """Test that the list of genres can be retrieved with pagination."""
        genre_factory.create_batch(5)
        response = api_client.get(self.GENRE_LIST_URL, {"limit": 1})
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_list_with_filter_name_success(self, api_client, genre_factory):
        """Test that the list of genres can be filtered by name."""
        genre_factory.create_batch(5)
        filter_genre = genre_factory(name="NonExistingName")
        response = api_client.get(
            f"{self.GENRE_LIST_URL}",
            {"name": filter_genre.name},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert len(response.data["results"]) == 1

    def test_list_with_ordering_by_name_success(self, api_client, genre_factory):
        """Test that the list of genres can be ordered by name."""
        genres = genre_factory.create_batch(5)
        ordered_genres = sorted(genres, key=lambda genre: genre.name.lower())

        response = api_client.get(
            f"{self.GENRE_LIST_URL}",
            {"ordering": "name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["id"] == ordered_genres[0].id

        response = api_client.get(
            f"{self.GENRE_LIST_URL}",
            {"ordering": "-name"},
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][-1]["id"] == ordered_genres[0].id

    def test_retrieve_success(self, api_client, genre):
        """Test that a genre can be retrieved."""
        response = api_client.get(self._get_book_detail_url(genre.id))
        assert response.status_code == status.HTTP_200_OK

    def test_create_not_as_admin_fail(self, auth_api_client):
        """Test that a genre can't be created for users that are not admin."""
        response = auth_api_client.post(self.GENRE_LIST_URL, {})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_not_as_admin_fail(self, auth_api_client, genre):
        """Test that a genre can't be updated for users that are not admin."""
        response = auth_api_client.put(
            self._get_book_detail_url(genre.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_part_update_not_as_admin_fail(self, auth_api_client, genre):
        """Test that a genre can't be partially updated for users that are not admin."""
        response = auth_api_client.patch(
            self._get_book_detail_url(genre.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_not_as_admin_fail(self, auth_api_client, genre):
        """Test that a genre can't be deleted for users that are not admin."""
        response = auth_api_client.delete(self._get_book_detail_url(genre.id))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_as_admin_success(self, admin_api_client):
        """Test that a genre can be created for users that are admin."""
        payload = {"name": "Test"}
        response = admin_api_client.post(self.GENRE_LIST_URL, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_as_admin_success(self, admin_api_client, genre):
        """Test that a genre can be updated for users that are admin."""
        payload = {"name": "Test"}
        response = admin_api_client.put(
            self._get_book_detail_url(genre.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_part_update_as_admin_success(self, admin_api_client, genre):
        """Test that a genre can be partially updated for users that are admin."""
        payload = {"name": "Test"}
        response = admin_api_client.patch(
            self._get_book_detail_url(genre.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_delete_as_admin_success(self, admin_api_client, genre):
        """Test that a genre can be deleted for users that are admin."""
        response = admin_api_client.delete(self._get_book_detail_url(genre.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class TestBookViewSet:
    """Tests for the BookViewSet."""

    BOOK_LIST_URL = reverse("books:book-list")

    def _get_book_detail_url(self, id):
        return reverse("books:book-detail", args=[id])

    def _get_book_upload_image_url(self, id):
        return reverse("books:book-upload-image", args=[id])

    def test_list_success(self, api_client):
        """Test that the list of books can be retrieved."""
        response = api_client.get(self.BOOK_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated(self, api_client, book_factory):
        """Test that the list of books can be retrieved with pagination."""
        book_factory.create_batch(5)
        response = api_client.get(self.BOOK_LIST_URL, {"limit": 1})
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_retrieve_success(self, api_client, book):
        """Test that a book can be retrieved."""
        response = api_client.get(self._get_book_detail_url(book.id))
        assert response.status_code == status.HTTP_200_OK

    def test_create_not_as_admin_fail(self, auth_api_client):
        """Test that a book can't be created for users that are not admin."""
        response = auth_api_client.post(self.BOOK_LIST_URL, {})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_not_as_admin_fail(self, auth_api_client, book):
        """Test that a book can't be updated for users that are not admin."""
        response = auth_api_client.put(
            self._get_book_detail_url(book.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_part_update_not_as_admin_fail(self, auth_api_client, book):
        """Test that a book can't be partially updated for users that are not admin."""
        response = auth_api_client.patch(
            self._get_book_detail_url(book.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_not_as_admin_fail(self, auth_api_client, book):
        """Test that a book can't be deleted for users that are not admin."""
        response = auth_api_client.delete(self._get_book_detail_url(book.id))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_upload_image_not_as_admin_fail(self, auth_api_client, book):
        """Test that an image can't be uploaded for users that are not admin."""
        response = auth_api_client.post(
            self._get_book_upload_image_url(book.id), {}, format="json"
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_as_admin_success(
        self,
        admin_api_client,
        author_factory,
        genre_factory,
    ):
        """Test that a book can be created for users that are admin."""
        authors = author_factory.create_batch(2)
        genres = genre_factory.create_batch(2)
        authors_ids = [author.id for author in authors]
        genres_ids = [genre.id for genre in genres]

        payload = {
            "title": "Test",
            "publication_date": "2000-01-01",
            "authors": authors_ids,
            "genres": genres_ids,
        }
        response = admin_api_client.post(self.BOOK_LIST_URL, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_as_admin_success(
        self, admin_api_client, book, author_factory, genre_factory
    ):
        """Test that a book can be updated for users that are admin."""
        authors = author_factory.create_batch(2)
        genres = genre_factory.create_batch(2)
        authors_ids = [author.id for author in authors]
        genres_ids = [genre.id for genre in genres]
        payload = {
            "title": "NewName",
            "publication_date": "2000-01-01",
            "authors": authors_ids,
            "genres": genres_ids,
        }

        response = admin_api_client.put(
            self._get_book_detail_url(book.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_part_update_as_admin_success(self, admin_api_client, book):
        """Test that a book can be partially updated for users that are admin."""
        payload = {
            "title": "NewName",
            "publication_date": "2000-01-01",
        }
        response = admin_api_client.patch(
            self._get_book_detail_url(book.id), payload, format="json"
        )
        assert response.status_code == status.HTTP_200_OK

    def test_delete_as_admin_success(self, admin_api_client, book):
        """Test that a book can be deleted for users that are admin."""
        response = admin_api_client.delete(self._get_book_detail_url(book.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_upload_image_as_admin_success(
        self, admin_api_client, book, temp_image_file
    ):
        """Test that an image can be uploaded for users that are admin."""
        with open(temp_image_file, "rb") as img:
            response = admin_api_client.put(
                self._get_book_upload_image_url(book.id),
                {"image": img},
                format="multipart",
            )

        assert response.status_code == status.HTTP_200_OK
        book.refresh_from_db()

        assert book.image is not None
        os.remove(book.image.path)
