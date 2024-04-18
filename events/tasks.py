from celery import shared_task
from django.core.mail import send_mail

@shared_task()
def send_event_notification_email(email_addresses:list, event_name:str, event_date:str):
    send_mail(
        f"{event_name} reminder",
        f"Hello! We hope this email finds you well. We wanted to send you a friendly reminder about the upcoming event, {event_name}, scheduled to take place at {event_date}",
        "event.manager@example.com",
        email_addresses,
        fail_silently=False,
    )