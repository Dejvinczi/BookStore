from django.core import mail


class TestMail:
    """Test system mail functionality."""

    def test_send_mail(self):
        """Test that the send_mail function sends an email."""
        email_data = {
            "subject": "test subject",
            "message": "test message",
            "from_email": "test@example.com",
            "recipient_list": ["test_recpieint@example.com"],
            "fail_silently": False,
        }

        mail.send_mail(**email_data)

        assert len(mail.outbox) == 1

        email = mail.outbox[0]

        assert email.subject == email_data["subject"]
        assert email.body == email_data["message"]
        assert email.from_email == email_data["from_email"]
        assert email.to == email_data["recipient_list"]
