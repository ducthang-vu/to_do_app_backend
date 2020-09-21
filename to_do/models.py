from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    user = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    priority = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(2)])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'do_do_tasks'
        unique_together = 'user', 'title'
