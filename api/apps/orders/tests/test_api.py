import pytest

# from django.core import mail
from django.urls import reverse
from django.utils.translation import gettext as _


@pytest.mark.django_db(transaction=True)
class TestOrderViewSet:
    """Test OrderViewSet."""

    ORDER_LIST_URL = reverse("orders:order-list")

    def get_detail_url(self, order):
        """Get order detail url."""
        return reverse("orders:order-detail", args=[order.id])

    def test_list_success(self, user, auth_api_client, order_factory):
        """Test list orders success."""
        orders = order_factory.create_batch(5, user=user)

        response = auth_api_client.get(
            self.ORDER_LIST_URL,
            params={"limit": 10},
            format="json",
        )
        response_orders = response.data["results"]

        assert response.status_code == 200
        assert len(response_orders) == 5

        orders_ids = {order.id for order in orders}
        response_orders_ids = {order["id"] for order in response_orders}

        assert orders_ids == response_orders_ids

    def test_list_only_current_user_orders_success(
        self, user, user_factory, auth_api_client, order_factory
    ):
        """Test list only current user orders success."""
        user_orders = order_factory.create_batch(5, user=user)
        diffrent_user = user_factory()
        order_factory.create_batch(5, user=diffrent_user)

        response = auth_api_client.get(
            self.ORDER_LIST_URL,
            params={"limit": 10},
            format="json",
        )
        response_orders = response.data["results"]

        assert response.status_code == 200
        assert len(response_orders) == 5

        orders_ids = {order.id for order in user_orders}
        response_orders_ids = {order["id"] for order in response_orders}

        assert orders_ids == response_orders_ids

    def test_retrieve_success(self, user, auth_api_client, order_factory):
        """Test retrieve single user order success."""
        order = order_factory(user=user)

        response = auth_api_client.get(self.get_detail_url(order), format="json")

        assert response.status_code == 200
        assert response.data["id"] == order.id

    def test_create_success(
        self,
        user,
        cart_item_factory,
        auth_api_client,
        order_model,
        settings,
        mailoutbox,
    ):
        """Test create new order based on user cart success."""

        cart = user.cart
        cart_item_factory.create_batch(2, cart=cart)
        cart_total_price = cart.total_price
        payload = {"address": "123 Main St"}

        response = auth_api_client.post(
            self.ORDER_LIST_URL,
            data=payload,
            format="json",
        )

        assert response.status_code == 201
        assert response.data["address"] == payload["address"]

        order_id = response.data["id"]
        order = order_model.objects.get(id=order_id)

        assert order.user == user
        assert order.address == payload["address"]
        assert order.status == order_model.StatusChoices.IN_PROGRESS
        assert order.total_price == cart_total_price
        assert order.items.count() == 2
        assert len(mailoutbox) == 1

        email = mailoutbox[0]

        assert email.subject == f"Order {order.no} changed status"
        expected_body = f"""\
        Hello {user.username},

        Your order {order.no} has changed status to: {order.status}\
        """
        assert email.body == expected_body
        assert email.from_email == settings.DEFAULT_FROM_EMAIL
        assert email.to == [user.email]

    def test_create_with_empty_cart_fail(self, auth_api_client):
        """Test create new order with empty cart fail."""
        payload = {"address": "123 Main St"}

        response = auth_api_client.post(
            self.ORDER_LIST_URL,
            data=payload,
            format="json",
        )

        assert response.status_code == 400
        assert response.data["detail"] == _("Cart is empty")
