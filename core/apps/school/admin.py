from django.contrib import admin
from .models import School
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
   """
    Admin configuration for the School model.
   """
   list_display = ("name", "latitude", "longitude","created_at", "updated_at")
   search_fields = ("name",)
   ordering = ("name",)
   