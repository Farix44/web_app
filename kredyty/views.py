from django.shortcuts import render, get_object_or_404, redirect
from .models import Loans, Clients
# from .forms import LoansForm
from django.contrib.auth.decorators import login_required
# import datetime
from datetime import datetime, timedelta
from .load_json import ConfigData
from kredyty.validators.loan_validation_hour import LoanValidationHour
from kredyty.validators.check_loan_validators import CheckLoanValidators
from kredyty.calculators.repayment_amount_calculator import RepaymentAmountCalculator
from django import forms

# REST_FRAMEWORK:
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoansSerializer, ClientsSerializer, LoansSerializerPUT
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions)
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()   # co chcemy wybierac z bd
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )

class LoansViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        if CheckLoanValidators().validate() == True:
            loan = request.data
            loan = loan.copy()
            loan['repayment_amount'] = RepaymentAmountCalculator(int(request.data["amount"]), float(ConfigData().get_data()['interest_rate'])).calculate()
            print(loan)
            serializer = LoansSerializer(data=loan)
            serializer.is_valid(raise_exception=True)    # validuje request
            self.perform_create(serializer)   # zapisuje do bazy
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            pass

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        mod_data = request.data
        mod_data = mod_data.copy()
        mod_data['repayment_amount'] = RepaymentAmountCalculator(int(request.data["amount"]), float(ConfigData().get_data()['interest_rate'])).calculate()
        serializer = LoansSerializerPUT(instance, data=mod_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

# PONIEZEJ FUNKCJE DO PRZEPISANIA

def loan_list(request):
    all_loans = Loans.objects.all()
    return render(request, 'kredyty.html', {'loans': all_loans})

@login_required
def new_loan(request):
    form = LoansForm(request.POST or None, request.FILES or None)
    form.fields['interest_rate'].widget = forms.HiddenInput()
    form.fields['repayment_amount'].widget = forms.HiddenInput()

    if form.is_valid():
        post = form.save(commit=False)
        repayment_amount = int(form['amount'].value()) * int(form['interest_rate'].value()) / 100 + int(form['amount'].value())
        post.repayment_amount = repayment_amount
        post.save
        form.save()
        return redirect(loan_list)

    if CheckLoanValidators().validate() == True:
        # return render(request, 'loan_form.html', {'form': form})
        return render(request, 'loan_form.html', {'form': form, 'interest_rate': ConfigData().get_data()['interest_rate']})
    else:
        return render(request, 'wrong_hour.html')

@login_required
def edit_loan(request, id):
    loan = get_object_or_404(Loans, pk=id)
    form = LoansForm(request.POST or None, request.FILES or None,
                     instance=loan)

    if form.is_valid():
        form.save()
        return redirect(loan_list)
    return render(request, 'loan_form.html', {'form': form})

@login_required
def delete_loan(request, id):
    loan = get_object_or_404(Loans, pk=id)

    if request.method == "POST":
        loan.delete()
        return redirect(loan_list)

    return render(request, 'confirm.html', {'loan': loan})
