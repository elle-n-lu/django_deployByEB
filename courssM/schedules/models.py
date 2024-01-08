from django.db import models
from django.conf import settings

# Create your models here.

class Schedules(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    # sche_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='schedule_creator')


    def __str__(self):
        return f"{self.date} - {self.time}"