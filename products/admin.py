from django.contrib import admin
from .models import Product
import requests
import os


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'stock', 'image')

    def save_model(self, request, obj, form, change):
        print("🔥 SAVE_MODEL CALLED 🔥")
        print("FILES:", request.FILES)

        file = request.FILES.get('image')

        if file:
            print("🚀 FILE DETECTED")

            file_name = file.name
            SUPABASE_URL = os.getenv("SUPABASE_URL")
            SUPABASE_KEY = os.getenv("SUPABASE_KEY")

            upload_url = f"{SUPABASE_URL}/storage/v1/object/media/{file_name}"

            response = requests.put(
                upload_url,
                headers={
                    "Authorization": f"Bearer {SUPABASE_KEY}",
                    "Content-Type": file.content_type,
                    "x-upsert": "true"
                },
                data=file.read()
            )

            print("STATUS:", response.status_code)
            print("TEXT:", response.text)

            if response.status_code in [200, 201]:
                obj.image_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{file_name}"

        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)

