from django.forms import ModelForm
from .models import Wnioski

class WnioskiForm(ModelForm):
    class Meta:
        model = Wnioski
        fields = ['kredytobiorca', 'kwota', 'okres']
