from django.forms import ModelForm, DateInput
from django import forms
from django.forms import ComboField
from .models import *
from .allocation_models import *
from django.forms.widgets import MultiWidget, CheckboxInput, TimeInput
from django.core.exceptions import ValidationError


class EditCourseSessionForm(forms.Form):
    allocations=forms.ModelChoiceField(
        queryset=  CourseAllocation.objects.all(),
        label="Select a course allocation",
    )


    day = forms.DateField(required=False,
        widget=forms.TimeInput(attrs={'type': 'date'}),
    )
    time=forms.TimeField(required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    tutor_confirm=forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
    )
    student_confirm=forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
    )
    
class CourseSessionForm(forms.Form):

    allocations=forms.ModelChoiceField(
        queryset=  CourseAllocation.objects.all(),
        label="Select a course allocation",
        # empty_label=None  # To make user selection required
    )

    repete_times=forms.IntegerField(initial=0)

    start_week_date = forms.DateField(required=False,
        widget=forms.TimeInput(attrs={'type': 'date','min':datetime.date.today()+datetime.timedelta(days=1)}),
    )   
    mondayCheck = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'value': 'Monday'}),
    )
    mondayTime = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    tuesdayCheck = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'value': 'Tuesday'}),
    )
    tuesdayTime =  forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )
    wendCheck = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'value': 'Wednesday'}),
    )
    wendTime =  forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    thurCheck = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'value': 'Thursday'}),
    )
    thurTime = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )
    fridayCheck = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'value': 'Friday'}),
    )
    fridayTime = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )
    repete_times=forms.IntegerField(initial=0)
        

