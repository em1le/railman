from django.urls import path

from project.views.main import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home")
]