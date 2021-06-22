from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Wnioski(models.Model):
    kredytobiorca = models.CharField(max_length=64)
    kwota = models.PositiveIntegerField(validators=[MinValueValidator(200), MaxValueValidator(10000)])
    okres = models.PositiveSmallIntegerField(default=6, validators=[MinValueValidator(1), MaxValueValidator(36)])

    def __str__(self):
        return 'kredyt na kwotę: ' + str(self.kwota)
