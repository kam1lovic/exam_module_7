from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import ProductModel


@admin.register(ProductModel)
class CustomUserAdmin(ModelAdmin):
    pass
