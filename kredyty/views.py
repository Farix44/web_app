from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Wnioski
from .forms import WnioskiForm

# Create your views here.

def lista_kredytow(request):
    wszystkie = Wnioski.objects.all()
    return render(request, 'kredyty.html', {'wnioski': wszystkie})

def nowy_wniosek(request):
    form = WnioskiForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(lista_kredytow)
    return render(request, 'wniosek_form.html', {'form': form})

def edytuj_wniosek(request, id):
    wniosek = get_object_or_404(Wnioski, pk=id)
    form = WnioskiForm(request.POST or None, request.FILES or None,
                       instance=wniosek)

    if form.is_valid():
        form.save()
        return redirect(lista_kredytow)
    return render(request, 'wniosek_form.html', {'form': form})

def usun_wniosek(request, id):
    wniosek = get_object_or_404(Wnioski, pk=id)

    if request.method == "POST":
        wniosek.delete()
        return redirect(lista_kredytow)

    return render(request, 'potwierdz.html', {'wniosek': wniosek})
