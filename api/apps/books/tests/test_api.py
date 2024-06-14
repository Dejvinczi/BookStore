import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestAuthorViewSet:
    """Tests for the AuthorViewSet."""

    AUTHOR_LIST_URL = reverse("books:author-list")

    def _get_book_detail_url(self, id):
        return reverse("books:author-detail", args=[id])

    def test_list_sucess(self, api_client):
        """Test that the list of authors can be retrieved."""
        response = api_client.get(self.AUTHOR_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated(self, api_client, author_factory):
        """Test that the list of authors can be retrieved with pagination."""
        author_factory.create_batch(5)
        response = api_client.get(f"{self.AUTHOR_LIST_URL}?limit=1")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_retrieve_sucess(self, api_client, author):
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

    def test_list_sucess(self, api_client):
        """Test that the list of genres can be retrieved."""
        response = api_client.get(self.GENRE_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated(self, api_client, genre_factory):
        """Test that the list of genres can be retrieved with pagination."""
        genre_factory.create_batch(5)
        response = api_client.get(f"{self.GENRE_LIST_URL}?limit=1")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_retrieve_sucess(self, api_client, genre):
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

    def test_list_sucess(self, api_client):
        """Test that the list of books can be retrieved."""
        response = api_client.get(self.BOOK_LIST_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_paginated(self, api_client, book_factory):
        """Test that the list of books can be retrieved with pagination."""
        book_factory.create_batch(5)
        response = api_client.get(f"{self.BOOK_LIST_URL}?limit=1")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 5
        assert len(response.data["results"]) == 1

    def test_retrieve_sucess(self, api_client, book):
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

    def test_update_as_admin_success(self, admin_api_client, book):
        """Test that a book can be updated for users that are admin."""
        payload = {
            "title": "NewName",
            "publication_date": "2000-01-01",
            "authors": [],
            "genres": [],
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
