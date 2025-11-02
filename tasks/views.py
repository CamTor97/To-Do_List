from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
# Create your views here.
def home(request):
    return render(request, "tasks/home.html")

# Creating the view for the List of Tasks
class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"