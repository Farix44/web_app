from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .load_json import ConfigData

# Create your models here.

class Loans(models.Model):
    # kredytobiorca = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    amount = models.PositiveIntegerField(default=200, validators=[MinValueValidator(ConfigData().get_data()['min_kwota']),
                                                                  MaxValueValidator(ConfigData().get_data()['max_kwota'])])
    period = models.PositiveSmallIntegerField(default=6, validators=[MinValueValidator(ConfigData().get_data()['min_okres']),
                                                                     MaxValueValidator(ConfigData().get_data()['max_okres'])])
    interest_rate = models.FloatField(default=ConfigData().get_data()['oprocentowanie'],
                                      validators=[MinValueValidator(ConfigData().get_data()['oprocentowanie']),
                                                   MaxValueValidator(ConfigData().get_data()['oprocentowanie'])])

    def __str__(self):
        return self.loan_record()

    def loan_record(self):
        return "{} {}: {}".format(self.first_name, self.second_name, self.amount)
