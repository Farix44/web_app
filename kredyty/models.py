from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .load_json import ConfigData

# For creating token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Adding token to just creted user
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Loans(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    amount = models.PositiveIntegerField(default=200, validators=[MinValueValidator(ConfigData().get_data()['min_amount']),
                                                                  MaxValueValidator(ConfigData().get_data()['max_amount'])])
    period = models.PositiveSmallIntegerField(default=6, validators=[MinValueValidator(ConfigData().get_data()['min_period']),
                                                                     MaxValueValidator(ConfigData().get_data()['max_period'])])
    interest_rate = models.FloatField(default=ConfigData().get_data()['interest_rate'],
                                      validators=[MinValueValidator(ConfigData().get_data()['interest_rate']),
                                                   MaxValueValidator(ConfigData().get_data()['interest_rate'])])
    repayment_amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.loan_record()

    def loan_record(self):
        return "{} {}: {}".format(self.first_name, self.second_name, self.amount)
