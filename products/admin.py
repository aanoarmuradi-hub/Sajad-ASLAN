from django.contrib import admin
from .models import Product
import requests
import os



SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


class ProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        file = request.FILES.get('image')

        if file:
            file_name = file.name

            upload_url = f"{SUPABASE_URL}/storage/v1/object/media/{file_name}"

            headers = {
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": file.content_type
            }

            response = requests.post(upload_url, headers=headers, data=file.read())

            if response.status_code == 200:
                obj.image_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{file_name}"
            else:
                print("Upload Error:", response.text)

        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)