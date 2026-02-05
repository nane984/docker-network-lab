import pytest
from unittest.mock import patch
from config.tasks.emails import send_welcome_email_task
from celery.exceptions import Retry

#Unit test taska
@pytest.mark.django_db      # Ovaj test SME da koristi bazu podataka
def test_send_welcome_email_task_calls_service():
    with patch("config.tasks.emails.send_welcome_email") as mock_send:
        send_welcome_email_task("test@example.com")

        mock_send.assert_called_once_with("test@example.com")


# eager test znaci da ne ceka delay() nego se izvrsava odmah. To smo u settings/test.py definisali
#Eager test - integrated test
@pytest.mark.django_db             # Ovaj test SME da koristi bazu podataka
def test_send_welcome_email_task_delay():
    with patch("config.tasks.emails.send_welcome_email") as mock_send:
        send_welcome_email_task.delay("test@example.com")

        mock_send.assert_called_once()


# retry test
@pytest.mark.django_db          # Ovaj test SME da koristi bazu podataka
def test_send_welcome_email_task_retries_on_exception():

    with patch(
        "config.tasks.emails.send_welcome_email",
        side_effect=Exception("SMTP error"),
    ) as mock_send:
        with pytest.raises(Exception):
            send_welcome_email_task("test@example.com")

        assert mock_send.call_count == 1