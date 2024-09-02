import pytest
from ..models import Cart, CartItem


@pytest.mark.django_db
class TestCartModel:
    """Tests for the Cart model."""

    @pytest.fixture(autouse=True)
    def cart_data(self, user_factory):
        user = user_factory()
        return {"user": user}

    def test_create_cart(self, cart_data):
        """Test that the Cart model can be created."""
        cart = Cart.objects.create(**cart_data)
        user = cart_data["user"]
        assert cart.id is not None
        assert cart.user == user

    def test_str(self, cart_data):
        """Test that the Cart model returns the correct string representation."""
        cart = Cart.objects.create(**cart_data)
        user = cart_data["user"]
        assert str(cart) == f"{user.username}'s cart"

    def test_total_price(self, cart_data, cart_item_factory):
        """Test that the total price is calculated correctly."""
        cart = Cart.objects.create(**cart_data)
        cart_items = cart_item_factory.create_batch(2, cart=cart)

        assert cart.total_price == sum(
            cart_item.total_price for cart_item in cart_items
        )


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

    def test_total_price(self, cart, book_factory):
        """Test that the total price is calculated correctly."""
        book = book_factory(price=100)
        cart_item = CartItem(cart=cart, book=book, quantity=3)
        assert cart_item.total_price == book.price * 3
