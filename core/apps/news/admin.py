from django.contrib import admin
from .models import News, NewsReceiver

# Register your models here.
class NewsInline(admin.TabularInline):
    model= News
    extra = 0
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
      Admin configuration for the News model.
   """
    list_display = ("title", "body", "created_by", "class_room", "created_at", "updated_at")
    search_fields = ("title", "class_room__name")
    list_filter = ("class_room", "created_at")
    
@admin.register(NewsReceiver)
class NewsReceiverAdmin(admin.ModelAdmin):
    """
        Admin configuration for the NewsReceiver 
    """
    list_display = ("news", "student", "is_read", "read_date")
    search_fields = ("news__title", "student__email")
    list_filter = ("is_read","read_date")
    