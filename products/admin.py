from django.contrib import admin
from .models import Product
import requests
import os
from .models import Category, SubCategory


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'stock', 'image','category', 'subcategory')

    def save_model(self, request, obj, form, change):
        print("🔥 hello broder 🔥")
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




class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'image')

    def save_model(self, request, obj, form, change):
        import os
        import requests

        file = request.FILES.get('image')

        if file:
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

            if response.status_code in [200, 201]:
                obj.image_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{file_name}"

        super().save_model(request, obj, form, change)
admin.site.register(Category, CategoryAdmin)




class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'category', 'image')

    def save_model(self, request, obj, form, change):
        import os
        import requests

        file = request.FILES.get('image')

        if file:
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

            if response.status_code in [200, 201]:
                obj.image_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{file_name}"

        super().save_model(request, obj, form, change)
        
admin.site.register(SubCategory, SubCategoryAdmin)

admin.site.site_header = "MyShop Admin"

admin.site.site_title = "MyShop Panel"

admin.site.index_title = "Welcome To MyShop Admin Panel"