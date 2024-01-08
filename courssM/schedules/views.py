from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Avg, Max, Min, Count
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .forms import *
from .models import *

@login_required
def add_event(request):
    if request.method == 'POST':
        form = SchedulesForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)  # Create the event object but don't save it yet
            event.sche_creator = request.user  # Set the creator based on the logged-in user
            event.save()
            messages.success(request,  ' event has been created.')
            return redirect('schedules')
        else:
            messages.error(request, 'Correct the error(S) below.')
    else:
        form = SchedulesForm()
    return render(request, 'schedules/add_event.html', {'form': form})

@login_required
def calendar_view(request):
    events = Schedules.objects.all()

    # program_filter = request.GET.get('program_filter')
    # if program_filter:
    #     programs = Program.objects.filter(title__icontains=program_filter)

    return render(request, 'schedules/calendar.html', {
        'title': "Canlendar | DjangoSMS",
        'events':events
    })