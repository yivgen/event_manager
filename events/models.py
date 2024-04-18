from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    organizer = models.CharField(max_length=300, null=False, blank=False)
    registered_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        blank=True,
        related_name='event_set'
    )

