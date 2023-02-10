from django.views.generic import ListView

from project.models import Track


class TrackListView(ListView):
    model = Track
    template_name = "track_list.html"
