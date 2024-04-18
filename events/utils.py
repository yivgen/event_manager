from users.models import MyUser
from events.models import Event
from event_manager.celery import app
from celery.schedules import crontab
from events.tasks import send_event_notification_email
from datetime import datetime, timedelta

def schedule_event_notification(event: Event, user: MyUser):
    send_event_notification_email.apply_async(
        args=[
            [user.email], 
            event.title, 
            event.date.isoformat()
        ],
        eta=event.date - timedelta(hours=1)
    )