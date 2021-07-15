from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .load_json import ConfigData

# Create your models here.

class Loans(models.Model):
    # kredytobiorca = models.CharField(max_length=64)
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    kwota = models.PositiveIntegerField(default=200, validators=[MinValueValidator(ConfigData().get_data()['min_kwota']),
                                                                 MaxValueValidator(ConfigData().get_data()['max_kwota'])])
    okres = models.PositiveSmallIntegerField(default=6, validators=[MinValueValidator(ConfigData().get_data()['min_okres']),
                                                                    MaxValueValidator(ConfigData().get_data()['max_okres'])])
    oprocentowanie = models.FloatField(default=ConfigData().get_data()['oprocentowanie'],
                                       validators=[MinValueValidator(ConfigData().get_data()['oprocentowanie']),
                                                   MaxValueValidator(ConfigData().get_data()['oprocentowanie'])])

    def __str__(self):
        return self.wniosek_rekord()

    def wniosek_rekord(self):
        return "{} {}: {}".format(self.imie, self.nazwisko, self.kwota)
