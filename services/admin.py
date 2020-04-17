from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'added']
    list_display_links = ['title', 'author']
    list_filter = ['title', 'added']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Services, ServicesAdmin)