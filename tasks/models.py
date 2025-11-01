from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    due_date = models.DateField(default=date.today, verbose_name="Due Date")
    is_completed = models.BooleanField(default=False, verbose_name="Completed")

    def __str__(self):
        return self.name