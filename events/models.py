from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    organizer = models.CharField(max_length=300, null=False, blank=False)

