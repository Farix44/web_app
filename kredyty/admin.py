from django.contrib import admin
from .models import Wnioski
# Register your models here.

admin.site.register(Wnioski)
# @admin.register(Wnioski)
# class WnioskiAdmin(admin.ModelAdmin):
#     list_display = ["kredytobiorca", "kwota", "okres"]
#     list_filter = ("kredytobiorca", "kwota", "okres")
#     search_fields = ("kredytobiorca", "kwota", "okres")
