from django.shortcuts import render, redirect
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView, View)
from django.urls import reverse_lazy
from .models import (Task, Project)
from .forms import ProjectCreationForm, TaskCreationForm, TaskFormSet
from django.db import transaction
# Create your views here.
def home(request):
    return render(request, "")

class DashboardView(TemplateView):
    template_name = "tasks/dashboard.html"

# Creating views for Project model
class ProjectListView(ListView):
    model = Project
    template_name = "tasks/project/projects.html"
    context_object_name = "projects"

class ProjectCreationView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "tasks/project/projects-create.html"
    success_url = reverse_lazy("projects")

    # def get(self, request):
    #     context = {
    #         "form": ProjectCreationForm(),
    #         "formset": TaskFormSet(queryset=Task.objects.none())
    #     }
    #     return render(request, self.template_name, context)
    
    # def post(self, request):
    #     project_form = ProjectCreationForm(request.POST)
    #     formset = TaskFormSet(request.POST)
    #     if project_form.is_valid() and formset.is_valid():
    #         with transaction.atomic():
    #             project_instance = project_form.save()
    #             tasks_instances = formset.save()
    #             for instance in tasks_instances:
    #                 instance.project = project_instance
    #                 instance.save()
    #         return redirect(self.success_url)
    #     context = {"form": project_form, "formset": formset}
    #     return render(request, self.template_name, context)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "tasks/project/projects-create.html"
    success_url = reverse_lazy("projects")

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
    template_name = "tasks/task/tasks.html"
    context_object_name = "tasks"

class TaskCreationView(CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "tasks/task/tasks-create.html"
    success_url = reverse_lazy("tasks")

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