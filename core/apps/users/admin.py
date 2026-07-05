from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active","is_superuser")
    list_filter = ("is_staff", "is_active", "is_registered")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff","is_superuser", "is_active", "is_registered", "groups", "user_permissions")})
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields" : (
                "email", "password1", "password2", "is_staff", 
                "is_superuser", "is_active", "groups", "user_permissions"
                )}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)