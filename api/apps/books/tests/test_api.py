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
