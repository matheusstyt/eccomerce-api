from django.contrib import admin

from products.models import *


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'amount',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(ProductModel, Products)
class Reviews(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(ReviewModel, Reviews)
class PriceHistory(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value',)
    search_fields = ('value',)
    list_per_page = 20

admin.site.register(PriceHistoryModel, PriceHistory)
