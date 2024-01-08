from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import EventAbstract
from django.conf import settings
from course.models import *

class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self,creator):
        events = Event.objects.filter(
            creator=creator, 
            is_active=True, is_deleted=False)
        return events

    def get_running_events(self,creator):
        running_events = Event.objects.filter(
            creator=creator,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events


class Event(EventAbstract):
    """ Event model """
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    created_by=models.DateTimeField(auto_now_add=True)
    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
