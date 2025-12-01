from django.shortcuts import render
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView, View)
from django.urls import reverse_lazy
from .models import (Task, Project)
# Create your views here.
def home(request):
    return render(request, "")

# Creating views for Project model
class ProjectListView(ListView):
    model = Project
    template_name = ""
    context_object_name = "projects"

class ProjectCreationView(View):
    template_name = ""
    success_url = reverse_lazy("")

class ProjectUpdateView(View):
    template_name = ""
    success_url = reverse_lazy("")

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = ""
    success_url = reverse_lazy("")

class ProjectDetailView(DetailView):
    model = Project
    template_name = ""
    context_object_name = "project_details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding Tasks for this project
        context["project_tasks"] = Task.objects.filter(project=self.object)
        return context




# Creating views for Task model
class TaskListView(ListView):
    model = Task
    template_name = ""
    context_object_name = "tasks"

class TaskCreationView(CreateView):
    model = Task
    form_class = ""
    template_name = ""
    success_url = ""

class TaskUpdateView(UpdateView):
    model = Task
    form_class = ""
    template_name = ""
    success_url = ""

class TaksDeleteView(DeleteView):
    model = Task
    template_name = ""
    success_url = ""

class TaskDetailView(DetailView):
    model = Task
    template_name = ""
    context_object_name = "task_details"