from django.urls import path
from kredyty.views import lista_kredytow, nowy_wniosek, edytuj_wniosek, usun_wniosek

urlpatterns = [
    path('lista/', lista_kredytow, name="lista_kredytow"),
    path('nowy/', nowy_wniosek, name="nowy_wniosek"),
    path('edytuj/<int:id>/', edytuj_wniosek, name="edytuj_wniosek"),
    path('usun/<int:id>/', usun_wniosek, name="usun_wniosek"),
]
