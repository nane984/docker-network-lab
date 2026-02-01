from celery import shared_task
from config.services.email_services import send_welcome_email

@shared_task (bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3})
def send_welcome_email_task(self, user_email):
    send_welcome_email(user_email)