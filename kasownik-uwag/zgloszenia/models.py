from django.db import models


class Dzial(models.Model):
    nazwa = models.CharField("nazwa", max_length=100, unique=True)
    opis = models.TextField("zakres odpowiedzialności")

    class Meta:
        verbose_name = "dział"
        verbose_name_plural = "działy"

    def __str__(self):
        return self.nazwa 


class Zgloszenie(models.Model):
    email = models.EmailField("adres e-mail pasażera")
    tresc = models.TextField("treść zgłoszenia")
    utworzono = models.DateTimeField("data zgłoszenia", auto_now_add=True)
    dzialy = models.ManyToManyField(
        Dzial,
        verbose_name="przypisane działy",
        related_name="zgloszenia",
        blank=True,
    )

    class Meta:
        verbose_name = "zgłoszenie"
        verbose_name_plural = "zgłoszenia"

    def __str__(self):  #
        return f"Zgłoszenie nr {self.pk}"