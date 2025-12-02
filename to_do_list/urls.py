"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name="tasks/home.html"), name='home'),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    # Project model URL's
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/create/", views.ProjectCreationView.as_view(), name="projects-create"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="projects-detail"),
    path("projects/<int:pk>/update/", views.ProjectUpdateView.as_view(), name="projects-update"),
    path("projects/<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="projects-delete"), 
    # Task model URL's 
    path("tasks/", views.TaskListView.as_view(), name='tasks-list'),
    path("tasks/create/", views.TaskCreationView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/<int:pk>/delete/", views.TaksDeleteView.as_view(), name="tasks-delete"),
]
