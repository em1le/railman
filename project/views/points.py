from typing import Dict

from django.db.models import Q
from django.utils import timezone
from django.views.generic import ListView, DetailView

from project.models import KilometerPoint


class KilometerPointListView(ListView):
    model = KilometerPoint
    template_name = "kilometer_point/kilometer_point_list.html"


class KilometerPointDetailView(DetailView):
    model = KilometerPoint
    template_name = "kilometer_point/kilometer_point_detail.html"

    def get_context_data(self, **kwargs) -> Dict:
        today = timezone.now()
        context = super().get_context_data(**kwargs)
        kilometer_point = self.get_object()
        events = kilometer_point.event_set.all()
        context["past_events"] = events.filter(date__lt=today.date())
        context["present_events"] = events.filter(date__date=today.date())
        context["future_events"] = events.filter(date__date__gt=today.date())
        return context