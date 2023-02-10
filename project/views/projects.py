from django.views.generic import ListView

from project.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"
