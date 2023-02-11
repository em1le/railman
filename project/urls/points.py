from django.urls import path

from project.views.points import KilometerPointListView, KilometerPointDetailView


urlpatterns = [
    path("", KilometerPointListView.as_view(), name="points-list"),
    path("details/<int:pk>", KilometerPointDetailView.as_view(), name="points-detail"),
]
