from django.contrib import admin
from .models import Loans, Clients
# Register your models here.

admin.site.register(Loans)
admin.site.register(Clients)
# @admin.register(Wnioski)
# class WnioskiAdmin(admin.ModelAdmin):
#     list_display = ["kredytobiorca", "kwota", "okres"]
#     list_filter = ("kredytobiorca", "kwota", "okres")
#     search_fields = ("kredytobiorca", "kwota", "okres")
