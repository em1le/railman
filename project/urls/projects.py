from django.urls import path

from project.views.projects import ProjectListView


urlpatterns = [
    path("", ProjectListView.as_view(), name="projects-list"),
]
