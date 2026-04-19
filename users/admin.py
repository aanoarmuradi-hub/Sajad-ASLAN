from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Role", {"fields": ("role",)}),
    )


admin.site.register(User, CustomUserAdmin)

