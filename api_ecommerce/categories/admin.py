from django.contrib import admin

from categories.models import CategoryModel

class Categories(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug', 'pai', 'created_at')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(CategoryModel, Categories)
