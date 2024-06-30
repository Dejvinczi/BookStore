import pytest
from ..models import Cart, CartItem


@pytest.mark.django_db
class TestCartModel:
    """Tests for the Cart model."""

    def test_create_cart(self, user):
        """Test that the Cart model can be created."""
        cart_data = {"user": user}
        cart = Cart.objects.create(**cart_data)
        assert cart.id is not None
        assert cart.user == user

    def test_str(self, user):
        """Test that the Cart model returns the correct string representation."""
        cart_data = {"user": user}
        cart = Cart.objects.create(**cart_data)
        assert str(cart) == f"{user.username}'s cart"

    def test_total_price(self, cart, book_factory):
        """Test that the total price is calculated correctly."""
        books = book_factory.create_batch(2)
        cart_item_arr = []
        for book in books:
            cart_item_arr.append(CartItem(cart=cart, book=book, quantity=3))
        CartItem.objects.bulk_create(cart_item_arr)
        assert cart.total_price == sum(book.price * 3 for book in books)


@pytest.mark.django_db
class TestCartItemModel:
    """Tests for the CartItem model."""

    def test_create_cart_item(self, cart, book):
        """Test that the CartItem model can be created."""

        cart_item_data = {"cart": cart, "book": book, "quantity": 1}
        cart_item = CartItem.objects.create(**cart_item_data)
        assert cart_item.id is not None
        assert cart_item.cart == cart
        assert cart_item.book == book
        assert cart_item.quantity == 1
