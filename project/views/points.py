from django.views.generic import ListView

from project.models import KilometerPoint


class KilometerPointListView(ListView):
    model = KilometerPoint
    template_name = "kilometer_point_list.html"
