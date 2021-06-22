from django.shortcuts import render
from django.http import HttpResponse
from .models import Wnioski

# Create your views here.

def lista_kredytow(request):
    wszystkie = Wnioski.objects.all()
    return render(request, 'kredyty.html', {'wnioski': wszystkie})
