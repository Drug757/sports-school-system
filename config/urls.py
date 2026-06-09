from django.contrib import admin
from django.urls import path
from schedule.views import lesson_list, create_lesson

from groups.views import group_list, create_group
from users.views import create_user, delete_user
from attendance.views import attendance_list, mark_attendance
from schedule.views import lesson_list
from attendance.views import mark_attendance

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', group_list),

    path('groups/', group_list),
    path('groups/create/', create_group),

    path('users/create/', create_user),
    path('users/delete/<int:user_id>/', delete_user),

    path('attendance/', attendance_list),
    path('attendance/create/', mark_attendance),
    path('attendance/mark/<int:lesson_id>/', mark_attendance),

    path('lessons/', lesson_list),
    path('lessons/create/', create_lesson),
]