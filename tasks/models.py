from django.db import models
from datetime import date

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    start_date = models.DateField(default=date.today, verbose_name="Start Date")
    end_date = models.DateField(blank=True, verbose_name="End Date")
    NOT_STARTED = "NS" 
    IN_PROGRESS = "IP"
    STANDBY = "SB"
    FINISHED = "FN"
    PROJECT_STATE_CHOICES = {
        NOT_STARTED: "Not Started",
        IN_PROGRESS: "In Progress",
        STANDBY: "In Standby",
        FINISHED: "Finished",
    }
    state = models.CharField(
        max_length=2,
        choices=PROJECT_STATE_CHOICES,
        default= NOT_STARTED,
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    start_date = models.DateField(default=date.today, verbose_name="Start Date")
    due_date = models.DateField(verbose_name="Due Date")
    NOT_STARTED = "NS" 
    IN_PROGRESS = "IP"
    STANDBY = "SB"
    FINISHED = "FN"
    TASK_STATE_CHOICES = {
        NOT_STARTED: "Not Started",
        IN_PROGRESS: "In Progress",
        STANDBY: "In Standby",
        FINISHED: "Finished",
    }
    state = models.CharField(
        max_length=2,
        choices=TASK_STATE_CHOICES,
        default= NOT_STARTED,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="project_tasks")

    def __str__(self):
        return self.name
    
