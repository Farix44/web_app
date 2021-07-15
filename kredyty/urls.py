from django.urls import path
from kredyty.views import loan_list, new_loan, edit_loan, delete_loan

urlpatterns = [
    path('lista/', loan_list, name="lista_kredytow"),
    path('nowy/', new_loan, name="nowy_wniosek"),
    path('edytuj/<int:id>/', edit_loan, name="edytuj_wniosek"),
    path('usun/<int:id>/', delete_loan, name="usun_wniosek"),
]
