from django.contrib import admin
from .models import Product
import requests
import os



class ProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        print("🔥 SAVE_MODEL CALLED 🔥")

        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)