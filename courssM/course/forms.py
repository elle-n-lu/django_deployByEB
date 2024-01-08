from itertools import chain
from django import forms
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import User

from accounts.models import *
from .models import Program, Course, CourseAllocation, Upload, UploadVideo

# User = settings.AUTH_USER_MODEL

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        self.fields['credit'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['program'].widget.attrs.update({'class': 'form-control'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['semester'].widget.attrs.update({'class': 'form-control'})


class CourseAllocationForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=User.objects.filter(is_student=True),
        label="Student",
        required=False
    )
    group = forms.ModelChoiceField(
        queryset=Student_Group.objects.all().order_by('group_name'),
        label="Group",
        required=False
    )
    
    courses = forms.ModelChoiceField(
        queryset=Course.objects.all().order_by('level'),
        label="courses",
    )
    lecturer = forms.ModelChoiceField(
        queryset=User.objects.filter(is_lecturer=True),
        label="lecturer",
    )
    course_length = forms.FloatField(
        min_value=0,
        initial=0,
        label="Course Length"
    )
    




class EditCourseAllocationForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all().order_by('level'),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    lecturer = forms.ModelChoiceField(
        queryset=User.objects.filter(is_lecturer=True),
        widget=forms.Select(attrs={'class': 'browser-default custom-select'}),
        label="lecturer",
    )
    student = forms.ModelChoiceField(
        queryset=User.objects.filter(is_student=True),
        widget=forms.Select(attrs={'class': 'browser-default custom-select'}),
        label="student",
    )

    class Meta:
        model = CourseAllocation
        fields = ['lecturer', 'courses','student']

    def __init__(self, *args, **kwargs):
        #    user = kwargs.pop('user')
        super(EditCourseAllocationForm, self).__init__(*args, **kwargs)
        self.fields['lecturer'].queryset = User.objects.filter(is_lecturer=True)
        self.fields['student'].queryset = User.objects.filter(is_student=True)


# Upload files to specific course
class UploadFormFile(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('title', 'file', 'course',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file'].widget.attrs.update({'class': 'form-control'})


# Upload video to specific course
class UploadFormVideo(forms.ModelForm):
    class Meta:
        model = UploadVideo
        fields = ('title', 'video', 'course',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['video'].widget.attrs.update({'class': 'form-control'})
