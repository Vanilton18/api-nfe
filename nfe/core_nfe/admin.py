from django.contrib import admin
from core_nfe import models
# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']