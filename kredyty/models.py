from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Wnioski(models.Model):
    kredytobiorca = models.CharField(max_length=64)
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    kwota = models.PositiveIntegerField(default=200, validators=[MinValueValidator(200),
                                                                 MaxValueValidator(10000)])
    okres = models.PositiveSmallIntegerField(default=6, validators=[MinValueValidator(1), MaxValueValidator(36)])
    oprocentowanie = models.FloatField(default=8)

    def __str__(self):
        return self.wniosek_rekord()

    def wniosek_rekord(self):
        return "{} {}: {}".format(self.imie, self.nazwisko, self.kwota)
