from django.urls import path
from kredyty.views import loan_list, new_loan, edit_loan, delete_loan

urlpatterns = [
    path('lista/', loan_list, name="loan_list"),
    path('nowy/', new_loan, name="new_loan"),
    path('edytuj/<int:id>/', edit_loan, name="edit_loan"),
    path('usun/<int:id>/', delete_loan, name="delete_loan"),
]
