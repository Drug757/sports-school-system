from django.db import models
from users.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)

    # Тренер группы
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trainer_groups"
    )

    # Участники группы
    participants = models.ManyToManyField(
        User, blank=True, related_name="participant_groups"
    )

    def __str__(self):
        return self.name
