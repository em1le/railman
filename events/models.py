from django.db import models


class Event(models.Model):

    name = models.CharField(
        max_length=32,
        verbose_name="Nom de l'évènement"
    )

    description = models.CharField(
        max_length=140,
        verbose_name="Description de l'évènement"
    )

    date = models.DateTimeField(
        verbose_name="Date de l'évènement"
    )

    kilometer_point = models.ForeignKey(
        "project.KilometerPoint",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Point kilométrique lié a l'évènement"
    )

    def __str__(self) -> str:
        return f"{self.name} | ID : {self.id}"

    class Meta:
        verbose_name = "Évènement"
        verbose_name_plural = "Évènements"
