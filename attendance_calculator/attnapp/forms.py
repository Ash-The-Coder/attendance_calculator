from django import forms
from .models import Semester, Subject, Attendance
from django.forms import DateInput

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SemesterForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['semester'].queryset = Semester.objects.filter(user=user)



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'semester', 'max_working_days']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SubjectForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['semester'].queryset = Semester.objects.filter(user=user)


class DateInput(forms.DateInput):
    input_type = 'date'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'subject', 'attendance_status', 'is_working_day']
        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AttendanceForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['subject'].queryset = Subject.objects.filter(user=user)