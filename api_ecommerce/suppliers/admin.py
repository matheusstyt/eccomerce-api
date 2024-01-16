from django.contrib import admin

from suppliers.models import SupplierModel

class Suppliers(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'address', 'phone')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(SupplierModel, Suppliers)
