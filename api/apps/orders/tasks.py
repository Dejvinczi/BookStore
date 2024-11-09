import logging
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Order

logger = logging.getLogger("api")


@shared_task
def send_order_change_status_email(order_id):
    """Send order change status email."""
    try:
        order = Order.objects.select_related("user").get(id=order_id)
        user = order.user
        recipient = user.email
        subject = f"Order {order.no} changed status"
        message = f"""\
        Hello {user.username},

        Your order {order.no} has changed status to: {order.status}\
        """
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, message, from_email, [recipient])
        logger.info(
            f"The email with order {order.no} status changed was sent to {recipient}."
        )

    except ObjectDoesNotExist:
        logger.error(f"The order with ID {order_id} does not exist in the database.")

    except Exception as exc:
        logger.error(
            f"An error occurred while sending the email with order "
            f"{order.no}: {str(exc)}"
        )
        send_order_change_status_email.retry(exc=exc, countdown=60, max_retries=3)
