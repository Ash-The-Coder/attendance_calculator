from django.db import models
from users.models import CustomUser

class Semester(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class Subject(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    max_working_days = models.IntegerField(default=0)
    # Add other fields related to the subject if needed

    def __str__(self):
        return f"{self.semester} - {self.name}"


class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attendance_status = models.BooleanField(default=False)
    is_working_day = models.BooleanField(default=True)
    # Add other fields related to the attendance if needed

    def __str__(self):
        return f"{self.subject} - {self.date} - {self.attendance_status}"
