from django.forms import ModelForm
from .models import Loans

class WnioskiForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['first_name', 'second_name', 'amount', 'period', 'interest_rate']
