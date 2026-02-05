import pytest
from unittest.mock import patch
from config.services.email_services import send_welcome_email

# Unit test

def test_send_welcome_email_calls_send_mail():
    with patch("config.services.email_services.send_mail") as mock_send:
        send_welcome_email("test@example.com") # poziv funkcije
        
        # proveravamo da je send_mail pozvan sa tačnim argumentima
        mock_send.assert_called_once_with(
            subject="Welcome!",
            message="Welcome to our platform!",
            from_email="noreply@example.com",
            recipient_list=["test@example.com"],
            fail_silently=False,
        )
