from django import forms
from .models import Project, Task
from django.forms.models import inlineformset_factory
from django.db.models import F


# Project model forms
class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date", "state"]

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"New Project"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Enter the details of your project"}),
            "start_date": forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            "state": forms.Select(attrs={"class":"form-control"})
        }

# Task model forms
class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "start_date", "due_date", "state", "project"]

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"New Task"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Enter the details of your task"}),
            "start_date": forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            "due_date": forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            "state": forms.Select(attrs={"class":"form-control"})
        }

TaskFormSet = inlineformset_factory(
    Project,
    Task,
    form = TaskCreationForm,
    extra = 1,
    can_delete = False
)

