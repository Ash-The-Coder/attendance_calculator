from django.contrib import admin

# Register your models here.

from .models import Semester, Subject, Attendance

admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Attendance)