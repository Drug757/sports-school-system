from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Админ'),
        ('trainer', 'Тренер'),
        ('student', 'Участник'),
    ]

    name = models.CharField(max_length=100)

    # теперь нельзя писать что угодно
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return f"{self.name} ({self.role})"