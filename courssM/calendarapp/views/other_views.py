# cal/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from calendarapp.models import  Event
from calendarapp.utils import Calendar
from calendarapp.forms import EventForm
from course.allocation_models import Course_Session

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = "calendarapp/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


@login_required(login_url="signup")
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/event.html", {"form": form})


class EventEdit(LoginRequiredMixin,generic.UpdateView):
    model = Event
    form_class = EventForm
    template_name = "calendarapp/event.html"

    def form_valid(self, form):
        # Perform any additional actions here before saving the form.
        # For example, you can add logging or other business logic.
        
        # Save the form instance and then redirect to 'dom.html'.
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # Define the URL to redirect to after a successful form submission.
        return '/schedules/'



@login_required
def event_singular(id):
    event = Event.objects.get(id=id)
    return event


@login_required
def event_details(request, event_id):
    event = event_singular(event_id)
    context = {"event": event, }
    return render(request, "calendarapp/event-details.html", context)


class CalendarViewNew(LoginRequiredMixin, generic.View):
    # login_url = "home"
    template_name = "calendarapp/calendarapp/calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        event_list = []
        events = Event.objects.all()
        for event in events:
            event_list.append(
                {   "id": event.id,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                    # "allocations": event.allocations,
                }
            )
        sessions=Course_Session.objects.all()
        datetime_format = "%Y-%m-%d%H:%M:%S"
        # for sess in sessions:
        #     combine_str=f"{sess.select_day}{sess.select_time}"
        #     start_time=datetime.strptime(combine_str, datetime_format)
        #     Event.objects.create(
        #        id=sess.id,
        #         title=sess.allocations,
        #         start_time=start_time,
        #         end_time=start_time+timedelta(hours=1),
        #         description=sess.delivered
        #     )
        # print('eve',event_list)
        context = {"form": forms, "events": event_list,
                #    "events_month": events_month
                   }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.creator = request.user
            form.save()
            messages.success(request,' event has been created.')
            return redirect("calendarapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


@login_required
def delete_event(request, event_id):
    program = Event.objects.get(pk=event_id)
    title = program.title
    program.delete()
    messages.success(request, 'Event ' + title + ' has been deleted.')

    return redirect('calendarapp:calendars')
    # event = get_object_or_404(Event, id=event_id)
    # if request.method == 'POST':
    #     event.delete()
    #     return JsonResponse({'message': 'Event sucess delete.'})
    # else:
    #     return JsonResponse({'message': 'Error!'}, status=400)
