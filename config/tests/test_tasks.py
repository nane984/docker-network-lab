import pytest
from unittest.mock import patch
from config.tasks.emails import send_welcome_email_task

#Unit test taska
@pytest.mark.django_db
def test_send_welcome_email_task_calls_service():
    with patch("config.tasks.emails.send_welcome_email") as mock_send:
        send_welcome_email_task("test@example.com")

        mock_send.assert_called_once_with("test@example.com")


#Eager test - integrated test
@pytest.mark.django_db
def test_send_welcome_email_task_delay():
    with patch("config.tasks.emails.send_welcome_email") as mock_send:
        send_welcome_email_task.delay("test@example.com")

        mock_send.assert_called_once()
