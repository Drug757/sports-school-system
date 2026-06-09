from django.shortcuts import render, redirect
from .models import Lesson
from .forms import LessonForm


def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'schedule/list.html', {'lessons': lessons})


def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/lessons/')
    else:
        form = LessonForm()

    return render(request, 'schedule/create.html', {'form': form})