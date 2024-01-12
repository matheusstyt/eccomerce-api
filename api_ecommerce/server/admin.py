from django.contrib import admin

# Register your models here.
from server.models import CategoryModel, PriceHistoryModel, ProductModel, ReviewModel, SupplierModel

class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'amount',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20
    
admin.site.register(ProductModel, Products)

class Suppliers(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'address', 'phone')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(SupplierModel, Suppliers)

class PriceHistory(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value',)
    search_fields = ('value',)
    list_per_page = 20

admin.site.register(PriceHistoryModel, PriceHistory)

class Categories(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug', 'pai', 'created_at')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(CategoryModel, Categories)

class Reviews(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(ReviewModel, Reviews)



