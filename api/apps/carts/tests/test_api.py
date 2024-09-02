import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestCartAPIView:
    """Tests for the Cart API."""

    CART_URL = reverse("carts:cart")

    def test_retrieve_empty_cart_success(self, auth_api_client):
        """Test that a user can retrieve their cart."""
        response = auth_api_client.get(self.CART_URL, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["items"]) == 0
        assert response.data["total_price"] == "0.00"

    def test_retrieve_nonempty_cart_success(
        self,
        user,
        auth_api_client,
        book_factory,
        cart_item_factory,
    ):
        """Test that a user can retrieve their cart."""
        cart = user.cart
        books = book_factory.create_batch(3)
        cart_items = [
            cart_item_factory(cart=cart, book=book, quantity=2) for book in books
        ]

        response = auth_api_client.get(self.CART_URL, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["items"]) == 3

        total_price = sum(
            [cart_item.quantity * cart_item.book.price for cart_item in cart_items]
        )

        assert response.data["total_price"] == str(total_price)


@pytest.mark.django_db
class TestCartItemViewSet:
    """Tests for CartItemViewSet."""

    CART_ITEM_LIST_URL = reverse("carts:cart-item-list")

    def _get_cart_item_detail_url(self, id):
        return reverse("carts:cart-item-detail", args=[id])

    def test_create_new_cart_item_success(
        self,
        user,
        auth_api_client,
        book_factory,
    ):
        """Test that a user can create a new cart item (add to cart new book)."""

        cart = user.cart
        book = book_factory()
        payload = {"book": book.id}

        response = auth_api_client.post(self.CART_ITEM_LIST_URL, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["quantity"] == 1

        cart_item = cart.items.first()

        assert cart_item.book == book
        assert cart_item.quantity == 1

    def test_create_existing_cart_item_success(
        self,
        user,
        auth_api_client,
        book_factory,
        cart_item_factory,
    ):
        """Test that a user can create a new cart item (add to cart existing book - increment quantity)."""

        cart = user.cart
        book = book_factory()
        cart_item = cart_item_factory(cart=cart, book=book, quantity=2)
        payload = {"book": book.id}

        response = auth_api_client.post(self.CART_ITEM_LIST_URL, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["quantity"] == 3

        cart_item.refresh_from_db()

        assert cart_item.quantity == 3

    def test_update_cart_item_quantity_success(
        self,
        user,
        auth_api_client,
        book_factory,
        cart_item_factory,
    ):
        """Test that a user can update the quantity of an existing cart item."""

        cart = user.cart
        book = book_factory()
        cart_item = cart_item_factory(cart=cart, book=book, quantity=2)
        payload = {"quantity": 3}

        response = auth_api_client.patch(
            self._get_cart_item_detail_url(cart_item.id),
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["quantity"] == 3

        cart_item.refresh_from_db()

        assert cart_item.quantity == 3

    def test_update_cart_item_quantity_to_zero_fail(
        self,
        user,
        auth_api_client,
        book_factory,
        cart_item_factory,
    ):
        """Test that a user cannot update the quantity of an existing cart item to zero."""

        cart = user.cart
        book = book_factory()
        cart_item = cart_item_factory(cart=cart, book=book, quantity=2)
        payload = {"quantity": 0}

        response = auth_api_client.patch(
            self._get_cart_item_detail_url(cart_item.id),
            payload,
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "quantity" in response.data

    def test_delete_cart_item_success(
        self,
        user,
        auth_api_client,
        book_factory,
        cart_item_factory,
    ):
        """Test that a user can delete an existing cart item."""

        cart = user.cart
        book = book_factory()
        cart_item = cart_item_factory(cart=cart, book=book, quantity=2)

        response = auth_api_client.delete(
            self._get_cart_item_detail_url(cart_item.id),
            format="json",
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert cart.items.count() == 0
