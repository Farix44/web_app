from django.forms import ModelForm
from .models import Loans

class WnioskiForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['imie', 'nazwisko', 'kwota', 'okres', 'oprocentowanie']
