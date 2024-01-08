import json
import pytz
from calendarapp.models import Event
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum, Avg, Max, Min, Count
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from accounts.models import User, Student
from accounts.decorators import lecturer_required, parent_required, student_required
from .forms import *
from .allocation_forms import *
from .models import *
from .allocation_models import *
from datetime import timedelta, datetime, date, timezone

def all_dates(selected_date,repete_times,weekday_index):
    today_date=datetime.now(pytz.timezone('Australia/Sydney')).date()
    if selected_date==today_date:
        selected_date = today_date+timedelta(days=1)  # Year, Month, Day
    end_date = selected_date + timedelta(weeks=repete_times)

    selected_dates = []

    while selected_date < end_date:
        if selected_date.weekday() ==weekday_index:  # 3 corresponds to Thursday (0 is Monday, 1 is Tuesday, and so on)
            selected_dates.append(selected_date)  # Add the date to the list  .strftime('%Y-%m-%d')
        selected_date += timedelta(days=1)
    return selected_dates

def saveCalendarEvent(a_date, select_time, selected_allocations,instance, allocation_length):
    datetime_format = "%Y-%m-%d%H:%M:%S"
    combine_str=f"{a_date}{select_time}"
    start_time=datetime.strptime(combine_str, datetime_format)
    Event.objects.create(
        title=selected_allocations,
        start_time=start_time,
        end_time=start_time+timedelta(hours=allocation_length),
        description=instance.delivered
    )


def deletCalendarEvent(a_date, select_time, selected_allocations,instance,allocation_length):
    datetime_format = "%Y-%m-%d%H:%M:%S"
    combine_str=f"{a_date}{select_time}"
    start_time=datetime.strptime(combine_str, datetime_format)
    event =  Event.objects.filter(
        title=selected_allocations,
        start_time=start_time,
        end_time=start_time+timedelta(hours=allocation_length),
        description=instance.delivered
    ).first()
    event.delete()

@login_required
@lecturer_required
def course_session_form(request):
    if request.method == 'POST':
        form = CourseSessionForm(request.POST)

        if form.is_valid():
            selected_allocations = form.cleaned_data.get('allocations')

            repete_times = form.cleaned_data.get('repete_times')
            start_week_date = form.cleaned_data.get('start_week_date')

            weekday_n={6: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday"}

            mondayCheck = form.cleaned_data.get('mondayCheck')
            mondayTime = form.cleaned_data.get('mondayTime')

            if mondayCheck:
                # Get today's date
                mondayCheckVal = form.fields['mondayCheck'].widget.attrs['value']
                target_weekday_index = next(key for key, value in weekday_n.items() if value == mondayCheckVal)
                totalDates=all_dates(start_week_date,repete_times, target_weekday_index)


                for i in totalDates:
                    select_time=mondayTime.strftime('%H:%M:%S')
                    instance = Course_Session(allocations=selected_allocations, select_day=i,select_time=select_time)
                    instance.save()

                    # save in calendar_event
                    saveCalendarEvent(i, select_time, selected_allocations,instance, selected_allocations.course_length)

            tuesdayCheck = form.cleaned_data.get('tuesdayCheck')
            tuesdayTime = form.cleaned_data.get('tuesdayTime')
            if tuesdayCheck:
                # Get today's date
                tuesCheckVal = form.fields['tuesdayCheck'].widget.attrs['value']
                target_weekday_index = next(key for key, value in weekday_n.items() if value == tuesCheckVal)

                totalDates=all_dates(start_week_date,repete_times, target_weekday_index)

                for i in totalDates:
                    select_time=tuesdayTime.strftime('%H:%M:%S')
                    instance = Course_Session(allocations=selected_allocations, select_day=i,select_time=select_time)
                    instance.save()

                    # save in calendar_event
                    saveCalendarEvent(i, select_time, selected_allocations,instance, selected_allocations.course_length)

            wendCheck = form.cleaned_data.get('wendCheck')
            wendTime = form.cleaned_data.get('wendTime')
            if wendCheck:
                # Get today's date
                wendCheckVal = form.fields['wendCheck'].widget.attrs['value']
                target_weekday_index = next(key for key, value in weekday_n.items() if value == wendCheckVal)

                totalDates=all_dates(start_week_date,repete_times, target_weekday_index)

                for i in totalDates:
                    select_time=wendTime.strftime('%H:%M:%S')
                    instance = Course_Session(allocations=selected_allocations, select_day=i,select_time=select_time)
                    instance.save()

                    # save in calendar_event
                    saveCalendarEvent(i, select_time, selected_allocations,instance,selected_allocations.course_length)

            thurCheck = form.cleaned_data.get('thurCheck')
            thurTime = form.cleaned_data.get('thurTime')
            if thurCheck:
                # Get today's date
                thurCheckVal = form.fields['thurCheck'].widget.attrs['value']
                target_weekday_index = next(key for key, value in weekday_n.items() if value == thurCheckVal)

                totalDates=all_dates(start_week_date,repete_times, target_weekday_index)

                for i in totalDates:
                    select_time=thurTime.strftime('%H:%M:%S')
                    instance = Course_Session(allocations=selected_allocations, select_day=i,select_time=select_time)
                    instance.save()

                    # save in calendar_event
                    saveCalendarEvent(i, select_time, selected_allocations,instance,selected_allocations.course_length)

            fridayCheck = form.cleaned_data.get('fridayCheck')
            fridayTime = form.cleaned_data.get('fridayTime')
            if fridayCheck:
                # Get today's date
                friCheckVal = form.fields['fridayCheck'].widget.attrs['value']
                target_weekday_index = next(key for key, value in weekday_n.items() if value == friCheckVal)

                totalDates=all_dates(start_week_date,repete_times, target_weekday_index)

                for i in totalDates:
                    select_time=fridayTime.strftime('%H:%M:%S')
                    instance = Course_Session(allocations=selected_allocations, select_day=i,select_time=select_time)
                    instance.save()

                    # save in calendar_event
                    saveCalendarEvent(i, select_time, selected_allocations,instance,selected_allocations.course_length)

            messages.success(request, 'session has been created.')
            return redirect('course_session')
        else:
            messages.error(request, 'Correct the error(s) below.')
    else:
        form = CourseSessionForm()

    return render(request, 'course/course_session_form.html', {
        'title': "Allocate Course Session | DjangoSMS",
        'form': form,
        # 'choices':DAYS_CHOICES
    }, )

@login_required
def course_session(request):
    if request.user.is_superuser:
        
        lecturer_filter = request.GET.get('lecturer')
        student_filter = request.GET.get('student')
        course_filter = request.GET.get('course')

        course_session=Course_Session.objects.all().order_by('select_day')
        studentOrGroup=User.objects.filter(first_name=student_filter,is_student=True).first() or Student_Group.objects.filter(group_name=student_filter).first()
        if student_filter and (not studentOrGroup):
                messages.error(request, 'student or group not found.')
        if lecturer_filter:
            course_session=course_session.filter(allocations__lecturer__first_name__icontains=lecturer_filter)
        if student_filter and studentOrGroup:
            if studentOrGroup._meta.model.__name__=='User':
                course_session=course_session.filter(allocations__content_objects_user=studentOrGroup)
            if studentOrGroup._meta.model.__name__=='Student_Group':
                course_session=course_session.filter(allocations__content_object_group=studentOrGroup)
        if course_filter:
            course_session=course_session.filter(allocations__courses__title__icontains=course_filter)
            
        course_sessions=course_session
        if not course_session:
                messages.error(request, 'no result found.')

    if request.user.is_lecturer:
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        course_sessions=Course_Session.objects.filter(allocations__lecturer=user).order_by('select_day')

    return render(request, 'course/course_session.html', {
        'title': "Allocate Course Session | DjangoSMS",
        'course_sessions':course_sessions
    }, )

@login_required
@parent_required
def course_session_parent(request,pk):
     if request.user.is_parent:
        user=User.objects.filter(id=pk).first()
        student = Student.objects.filter(student_id=pk).first()
        # personal sessions
        course_sessions = Course_Session.objects.filter(allocations__content_objects_user=user).order_by('created_time')
        # group sessions
        if student.student_group.id:
            student_group=Student_Group.objects.filter(id=student.student_group.id).first()
            group_sessions = Course_Session.objects.filter(allocations__content_object_group=student_group).order_by('created_time')

        return render(request, 'course/course_session.html', {
            'title': "Allocate Course Session | DjangoSMS",
            'course_sessions':course_sessions,
            'group_sessions':group_sessions
        }, )

@login_required
def course_session_edit(request, pk):
    course_session_singular = get_object_or_404(Course_Session, pk=pk)

    if request.method == 'POST':
        form = EditCourseSessionForm(request.POST)
        
        pre_a_date=course_session_singular.select_day
        pre_select_time=course_session_singular.select_time
        pre_selected_allocations=course_session_singular.allocations
        pre_instance=course_session_singular
        pre_allocation_length= pre_selected_allocations.course_length
        
        if form.is_valid():
            form_data=form.cleaned_data
            if request.user.is_superuser:

                course_session_singular.select_day = form_data['day']
                course_session_singular.select_time = form_data.get('time')
                course_session_singular.tutor_confirm = form_data['tutor_confirm']
                course_session_singular.student_confirm = form_data['student_confirm']
                course_session_singular.save()

                # update calendar event
                
                deletCalendarEvent(pre_a_date, pre_select_time, pre_selected_allocations,pre_instance,pre_allocation_length)

                up_a_date= course_session_singular.select_day
                up_select_time=course_session_singular.select_time
                up_selected_allocations = course_session_singular.allocations
                up_instance = course_session_singular
                up_allocation_length=up_selected_allocations.course_length
                saveCalendarEvent(up_a_date, up_select_time, up_selected_allocations,up_instance, up_allocation_length)

                

            if request.user.is_lecturer:
                course_session_singular.tutor_confirm = form_data['tutor_confirm']
                course_session_singular.save()

            if request.user.is_parent:
                course_session_singular.student_confirm = form_data['student_confirm']
                course_session_singular.save()

            if course_session_singular.tutor_confirm and course_session_singular.student_confirm:
                    course_session_singular.delivered=True
                    if course_session_singular.allocations.content_type.model_class().__name__ == 'Student_Group':
                        course_stu = Student_Group.objects.filter(id = course_session_singular.allocations.content_object.id).first()
                        students = Student.objects.filter(student_group_id=course_stu.id)
                        for i in students:
                            i.session_hours -= course_session_singular.allocations.course_length
                            i.save()
                    if course_session_singular.allocations.content_type.model_class().__name__ == 'User':
                        course_stu = Student.objects.filter(student_id = course_session_singular.allocations.content_object.id).first()
                        course_stu.session_hours -= course_session_singular.allocations.course_length
                        course_stu.save()
                    course_session_singular.save()

            if course_session_singular.delivered and (not course_session_singular.tutor_confirm or not course_session_singular.student_confirm):
                course_session_singular.delivered=False
                if course_session_singular.allocations.content_type.model_class().__name__ == 'Student_Group':
                    course_stu = Student_Group.objects.filter(id = course_session_singular.allocations.content_object.id).first()
                    students = Student.objects.filter(student_group_id=course_stu.id)
                    for i in students:
                        i.session_hours += course_session_singular.allocations.course_length
                        i.save()
                if course_session_singular.allocations.content_type.model_class().__name__ == 'User':
                    course_stu = Student.objects.filter(student_id = course_session_singular.allocations.content_object.id).first()
                    course_stu.session_hours += course_session_singular.allocations.course_length
                    course_stu.save()
                course_session_singular.save()


            messages.success(request, 'course session has been updated.')
            if request.user.is_parent:
                return redirect('student_list')
            return redirect('course_session')
    else:
        initial_data = {
            "allocations":course_session_singular.allocations,
            "day" :course_session_singular.select_day,
            "time" :course_session_singular.select_time,
            "tutor_confirm" :course_session_singular.tutor_confirm,
            "student_confirm" :course_session_singular.student_confirm,
        }
        form = EditCourseSessionForm(initial=initial_data)

    return render(request, 'course/course_session_form_edit.html', {
        'title': "Edit Course Session | DjangoSMS",
        'form': form
    }, )


@login_required
def del_course_session(request, pk):
    course_session =Course_Session.objects.filter(pk=pk).first()

    a_date= course_session.select_day
    select_time=course_session.select_time
    selected_allocations = course_session.allocations
    instance = course_session
    allocation_length=selected_allocations.course_length
    deletCalendarEvent(a_date, select_time, selected_allocations,instance,allocation_length)

    course_session.delete()
    messages.success(request, 'successfully deleted!')
    return redirect("course_session")