from django.urls import path
from . import views

urlpatterns = [
    # URLs for Semester model views
    path('semesters/', views.semester_list, name='semester_list'),
    path('semesters/create/', views.semester_create, name='semester_create'),
    path('semesters/<int:semester_id>/', views.semester_detail, name='semester_detail'),
    path('semesters/<int:semester_id>/update/', views.semester_update, name='semester_update'),
    path('semesters/<int:semester_id>/delete/', views.semester_delete, name='semester_delete'),

    # URLs for Subject model views
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subjects/<int:subject_id>/update/', views.subject_update, name='subject_update'),
    path('subjects/<int:subject_id>/delete/', views.subject_delete, name='subject_delete'),

    # URLs for Attendance model views
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/<int:attendance_id>/update/', views.attendance_update, name='attendance_update'),
    path('attendance/<int:attendance_id>/delete/', views.attendance_delete, name='attendance_delete'),

    path('subject_attendance/', views.subject_attendance, name='subject_attendance'),
]
