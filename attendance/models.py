from django.db import models
from users.models import User
from schedule.models import Lesson


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.lesson}"
