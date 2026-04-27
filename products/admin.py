from django.contrib import admin
from .models import Product
import requests
import os

class ProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        print("🔥 SAVE_MODEL CALLED 🔥")

        file = request.FILES.get('image')

        if file:
            file_name = file.name

            SUPABASE_URL = os.getenv("SUPABASE_URL")
            SUPABASE_KEY = os.getenv("SUPABASE_KEY")

            upload_url = f"{SUPABASE_URL}/storage/v1/object/media/{file_name}"

            headers = {
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": file.content_type
            }

            response = requests.post(upload_url, headers=headers, data=file.read())

            if response.status_code in [200, 201]:
                obj.image_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{file_name}"

        super().save_model(request, obj, form, change)


# 💥 مهم‌ترین خط:
admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)