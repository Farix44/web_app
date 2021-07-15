from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Loans
from .forms import WnioskiForm
from django.contrib.auth.decorators import login_required
# import datetime
from datetime import datetime, timedelta
import json
import os
from .load_json import ConfigData
from .loan_validation import LoanValidation

# Create your views here.

def loan_list(request):
    all_loans = Loans.objects.all()
    return render(request, 'kredyty.html', {'loans': all_loans})

@login_required
def new_loan(request):
    form = WnioskiForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(loan_list)

    curr_time = datetime.now() + timedelta(hours = ConfigData().get_data()['time_zone_difference'])   # timedelta - poprawka roznicy czasu
    factors = {}
    factors["hour"] = curr_time.hour

    if LoanValidation(factors).validate() == True:
        return render(request, 'wniosek_form.html', {'form': form})
    else:
        return render(request, 'zla_godzina.html')

@login_required
def edit_loan(request, id):
    loan = get_object_or_404(Loans, pk=id)
    form = WnioskiForm(request.POST or None, request.FILES or None,
                       instance=loan)

    if form.is_valid():
        form.save()
        return redirect(loan_list)
    return render(request, 'wniosek_form.html', {'form': form})

@login_required
def delete_loan(request, id):
    loan = get_object_or_404(Loans, pk=id)

    if request.method == "POST":
        loan.delete()
        return redirect(loan_list)

    return render(request, 'potwierdz.html', {'loan': loan})
