from django.urls import path
from kredyty.views import lista_kredytow

urlpatterns = [
    path('lista/', lista_kredytow)
]
