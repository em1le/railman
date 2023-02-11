from django.urls import path

from project.views.routes import RouteListView

urlpatterns = [
    path("", RouteListView.as_view(), name="routes-list"),
]