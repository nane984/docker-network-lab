from django.core.mail import send_mail


def send_welcome_email(user_email):
    
    send_mail(
        subject="Welcome!",
        message="Welcome to our platform!",
        from_email="noreply@example.com",
        recipient_list=[user_email],
        fail_silently=False,
    )
    