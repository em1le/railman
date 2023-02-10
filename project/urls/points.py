from django.urls import path

from project.views.points import KilometerPointListView


urlpatterns = [
    path("", KilometerPointListView.as_view(), name="points-list"),
]
