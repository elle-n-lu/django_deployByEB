from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='schedules'),
    path('add_event', views.add_event, name='add_event'),
]