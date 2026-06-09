from django.shortcuts import render, get_object_or_404, redirect
from schedule.models import Lesson
from .models import Attendance


def mark_attendance(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    students = lesson.group.participants.all()

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'student_{student.id}')

            Attendance.objects.update_or_create(
                lesson=lesson,
                student=student,
                defaults={
                    'present': status == 'present'
                }
            )

        return redirect('/attendance/')

    return render(request, 'attendance/mark.html', {
        'lesson': lesson,
        'students': students
    })


def attendance_list(request):
    attendance = Attendance.objects.select_related('student', 'lesson')
    return render(request, 'attendance/list.html', {'attendance': attendance})