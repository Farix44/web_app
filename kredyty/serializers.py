from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Loans

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LoansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loans
        fields = ['id', 'first_name', 'second_name', 'amount',
                  'period', 'interest_rate', 'repayment_amount']
