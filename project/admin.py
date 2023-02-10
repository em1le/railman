from django.contrib import admin

from project.models import Project, Route, Track, KilometerPoint


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    ...


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    ...


@admin.register(KilometerPoint)
class KilometerPointAdmin(admin.ModelAdmin):
    ...
