from unittest import mock
from django.core.exceptions import ObjectDoesNotExist
from ..tasks import send_order_change_status_email


@mock.patch("apps.orders.tasks.Order.objects")
@mock.patch("apps.orders.tasks.logger")
@mock.patch("apps.orders.tasks.send_mail")
def test_send_order_change_status_email_success(
    mock_send_mail, mock_logger, mock_order_objects, settings
):
    """Test send_order_change_status_email with success."""
    mock_user = mock.MagicMock(email="test@example.com", username="testuser")
    mock_order = mock.MagicMock(id=1, no="ORD-001", status="Shipped", user=mock_user)
    mock_order_objects.select_related.return_value.get.return_value = mock_order

    send_order_change_status_email(mock_order.id)

    mock_send_mail.assert_called_once_with(
        f"Order {mock_order.no} changed status",
        f"Hello {mock_user.username},\n\nYour order {mock_order.no} has changed status to: {mock_order.status}",
        settings.DEFAULT_FROM_EMAIL,
        [mock_user.email],
    )
    mock_logger.info.assert_called_once_with(
        f"The email with order {mock_order.no} status changed was sent to {mock_user.email}."
    )


@mock.patch("apps.orders.tasks.Order.objects")
@mock.patch("apps.orders.tasks.logger")
@mock.patch("apps.orders.tasks.send_mail")
def test_send_order_change_status_email_order_not_found_exception(
    mock_send_mail, mock_logger, mock_order_objects
):
    """Test send_order_change_status_email with ObjectDoesNotExist exception."""
    mock_order_objects.select_related.return_value.get.side_effect = ObjectDoesNotExist(
        "Order matching query does not exist."
    )

    send_order_change_status_email(999)

    mock_send_mail.assert_not_called()
    mock_logger.error.assert_called_once_with(
        f"The order with ID {999} does not exist in the database."
    )


@mock.patch("apps.orders.tasks.Order.objects")
@mock.patch("apps.orders.tasks.logger")
@mock.patch("apps.orders.tasks.send_mail")
@mock.patch("apps.orders.tasks.send_order_change_status_email.retry")
def test_send_order_change_status_email_unexpected_exception(
    mock_retry, mock_send_mail, mock_logger, mock_order_objects
):
    """Test send_order_change_status_email with an unexpected exception."""
    mock_user = mock.MagicMock(email="test@example.com", username="testuser")
    mock_order = mock.MagicMock(id=1, no="ORD-001", status="Shipped", user=mock_user)
    mock_order_objects.select_related.return_value.get.return_value = mock_order
    exception_msg = "Some unexpected error occurred."
    mock_send_mail.side_effect = Exception(exception_msg)

    send_order_change_status_email(mock_order.id)

    mock_logger.error.assert_called_once_with(
        f"An error occurred while sending the email with order {mock_order.no}: {exception_msg}"
    )
    mock_retry.assert_called_once_with(
        exc=mock_send_mail.side_effect, countdown=60, max_retries=3
    )
