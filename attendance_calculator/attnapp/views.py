from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Semester, Subject, Attendance
from .forms import SemesterForm, SubjectForm, AttendanceForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Semester, Subject, Attendance
from .forms import SemesterForm, SubjectForm, AttendanceForm

# Views for Semester model
# Implement similar views as for User (list, detail, create, update, delete)

@login_required
def semester_list(request):
    semesters = Semester.objects.filter(user=request.user)
    return render(request, 'semester_list.html', {'semesters': semesters})

@login_required
def semester_detail(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id, user=request.user)
    return render(request, 'semester_detail.html', {'semester': semester})

@login_required
def semester_create(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            semester = form.save(commit=False)
            semester.user = request.user
            semester.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'semester_form.html', {'form': form})

@login_required
def semester_update(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id, user=request.user)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('semester_detail', semester_id=semester_id)
    else:
        form = SemesterForm(instance=semester, user=request.user)
    return render(request, 'semester_form.html', {'form': form})

@login_required
def semester_delete(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id, user=request.user)
    if request.method == 'POST':
        semester.delete()
        return redirect('semester_list')
    return render(request, 'semester_confirm_delete.html', {'semester': semester})

# Similarly, modify the views for Subject and Attendance models using the login_required decorator.

# Views for Subject model
# Implement similar views as for User (list, detail, create, update, delete)

@login_required
def subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'subject_list.html', {'subjects': subjects})

@login_required
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id, user=request.user)
    return render(request, 'subject_detail.html', {'subject': subject})

@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, user=request.user)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(user=request.user)
    return render(request, 'subject_form.html', {'form': form})


@login_required
def subject_update(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id, user=request.user)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', subject_id=subject_id)
    else:
        form = SubjectForm(instance=subject, user=request.user)
    return render(request, 'subject_form.html', {'form': form})

@login_required
def subject_delete(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id, user=request.user)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject_confirm_delete.html', {'subject': subject})

# Views for Attendance model
# Implement similar views as for User (list, detail, create, update, delete)

# Views for Attendance model
@login_required
def attendance_list(request):
    attendances = Attendance.objects.filter(user=request.user)
    return render(request, 'attendance_list.html', {'attendances': attendances})

@login_required
def attendance_detail(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id, user=request.user)
    return render(request, 'attendance_detail.html', {'attendance': attendance})

@login_required
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST,user=request.user)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.user = request.user
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(user=request.user)
    return render(request, 'attendance_form.html', {'form': form})

@login_required
def attendance_update(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id, user=request.user)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('attendance_detail', attendance_id=attendance_id)
    else:
        form = AttendanceForm(instance=attendance, user=request.user)
    return render(request, 'attendance_form.html', {'form': form})

@login_required
def attendance_delete(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id, user=request.user)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendance_confirm_delete.html', {'attendance': attendance})

@login_required
def subject_attendance(request):
    # Get the subjects related to the current user
    subjects = Subject.objects.filter(user=request.user)

    subject_attendance_data = []
    for subject in subjects:
        attendance_records = Attendance.objects.filter(subject=subject, user=request.user)  # Filter by current user
        is_working_day = attendance_records.filter(is_working_day=1).count()
        present_days = attendance_records.filter(attendance_status=1).count()
        absent_days = attendance_records.filter(attendance_status=0).count()

        max_working_days = subject.max_working_days
        remaining_days = int((0.25 * max_working_days) - absent_days)

        subject_data = {
            'subject_name': subject.name,
            'is_working_day': is_working_day,
            'present_days': present_days,
            'absent_days': absent_days,
            'remaining_days': remaining_days,
        }
        subject_attendance_data.append(subject_data)

    context = {
        'subject_attendance_data': subject_attendance_data,
    }

    return render(request, 'subject_attendance.html', context)
