from django.urls import path

from project.views.tracks import TrackListView


urlpatterns = [
    path("", TrackListView.as_view(), name="tracks-list"),
]
