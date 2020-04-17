from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'added']
    list_display_links = ['title', 'slug']
    list_filter = ['title', 'added']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Products, ProductsAdmin)