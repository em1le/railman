from django.views.generic import ListView

from project.models import Route


class RouteListView(ListView):
    model = Route
    template_name = "routes/routes_list.html"
    