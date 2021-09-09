
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Loans, Clients

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)   # creater_user to wbudowana metoda, co pozwoli tworzyc uzytkownika z hashowanym haslem
        return user

class LoansSerializer(serializers.ModelSerializer):
    # client = ClientsSerializer(many=False)
    class Meta:
        model = Loans
        fields = ['id', 'amount', 'period', 'interest_rate', 'repayment_amount', 'client']
        # read_only_fields = ['client']

class ClientsSerializer(serializers.ModelSerializer):
    loans = LoansSerializer(many=True, read_only=True)
    class Meta:
        model = Clients
        fields = ['id', 'first_name', 'second_name', 'loans']



