from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from .models import CourseAllocation
from django.db.models import Q


class CourseSessionManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
                Q(allocations__lecturer__first_name__icontains=query) | 
                         Q(allocations__student__first_name__icontains=query)| 
                         Q(allocations__courses__title__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Course_Session(models.Model):
    """ Event model """

    allocations = models.ForeignKey(CourseAllocation, on_delete=models.CASCADE, related_name='event_allocation')

    start_week_date = models.DateField(max_length=50,blank=True,null=True)


    select_day=models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    # course_dates=ArrayField(models.JSONField(null=True, blank=True, default=dict), max_length=250, blank=True, default=[])
    select_time = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    repete_times = models.IntegerField(default=0)
    

    tutor_confirm=models.BooleanField(default=False)
    student_confirm=models.BooleanField(default=False)

    delivered=models.BooleanField(default=False)

    objects=CourseSessionManager()

    created_time=models.DateTimeField(auto_now_add=True)


