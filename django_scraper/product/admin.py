from django.contrib import admin
from .models import data

@admin.register(data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'url', 'image_url')