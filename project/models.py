from django.db import models


class Project(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="Nom du projet"
    )

    def __str__(self) -> str:
        return f"{self.name} | ID : {self.id}"

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"


class Route(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="Nom du trajet"
    )

    projects = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        verbose_name="Projet lié"
    )

    def __str__(self) -> str:
        return f"{self.name} | ID : {self.id}"

    class Meta:
        verbose_name = "Trajet"
        verbose_name_plural = "Trajets"


class Track(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="Nom de la voie"
    )

    routes = models.ManyToManyField(
        "project.Route",
        verbose_name="Route liée"
    )

    def __str__(self) -> str:
        return f"{self.name} | ID : {self.id}"

    class Meta:
        verbose_name = "Voie"
        verbose_name_plural = "Voies"


class KilometerPoint(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="Nom du Point Kilometrique"
    )

    tracks = models.ForeignKey(
        "project.Track",
        on_delete=models.CASCADE,
        verbose_name="Voie liée"
    )

    def __str__(self) -> str:
        return f"{self.name} | ID : {self.id}"

    class Meta:
        verbose_name = "Point kilometrique"
        verbose_name_plural = "Points kilometriques"

