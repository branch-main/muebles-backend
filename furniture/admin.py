from django.contrib import admin
from .models import Furniture, Provider


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'material', 'price', 'stock')
    list_filter = ('provider', 'material')
    search_fields = ('name', 'material')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'email')
    search_fields = ('name', 'city', 'email')
