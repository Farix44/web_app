from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Wnioski
from .forms import WnioskiForm
from django.contrib.auth.decorators import login_required
# import datetime
from datetime import datetime, timedelta
import json
import os

# Create your views here.

def lista_kredytow(request):
    wszystkie = Wnioski.objects.all()
    return render(request, 'kredyty.html', {'wnioski': wszystkie})

@login_required
def nowy_wniosek(request):
    form = WnioskiForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(lista_kredytow)

# dac to do zewnetrznej klasy
# plik z configem (json)
# dac klase co wyciaga wszystkie reguly z configa (lista regul, przechodzi je w petli, jak niespelnione to odmawia kredytu)

    # curr_time = datetime.datetime.now()
    # if curr_time.hour < 6:
    #     return render(request, 'zla_godzina.html')
    # else:
    #     return render(request, 'wniosek_form.html', {'form': form})

    jj = str()
    with open(os.path.join('kredyty', 'kredyty_config.json'), 'r') as f:
        jj = f.read()

    data = json.loads(jj)
    min_godz = data['min_godzina']
    max_godz = data['max_godzina']

    curr_time = datetime.now() + timedelta(hours = data['roznica_czasu_godz'])   # timedelta - poprawka roznicy czasu
    if ( curr_time.hour < min_godz or curr_time.hour > max_godz):
        return render(request, 'zla_godzina.html')
    else:
        return render(request, 'wniosek_form.html', {'form': form})

@login_required
def edytuj_wniosek(request, id):
    wniosek = get_object_or_404(Wnioski, pk=id)
    form = WnioskiForm(request.POST or None, request.FILES or None,
                       instance=wniosek)

    if form.is_valid():
        form.save()
        return redirect(lista_kredytow)
    return render(request, 'wniosek_form.html', {'form': form})

@login_required
def usun_wniosek(request, id):
    wniosek = get_object_or_404(Wnioski, pk=id)

    if request.method == "POST":
        wniosek.delete()
        return redirect(lista_kredytow)

    return render(request, 'potwierdz.html', {'wniosek': wniosek})
