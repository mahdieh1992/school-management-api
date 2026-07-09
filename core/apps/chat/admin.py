from django.contrib import admin
from .models import Message, MessageReceiver
# Register your models here.

class MessageReceiverInline(admin.TabularInline):
    model = MessageReceiver
    extra = 0
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Message model
    """
    list_display = ("text", "sender","created_at", "updated_at")
    search_fields = ("text", "sender__email")
    inlines = [MessageReceiverInline,]
    
@admin.register(MessageReceiver)
class MessageReceiverAdmin(admin.ModelAdmin):
    """
        Admin configuration for the MessageReceiver model
    """
    list_display = ("message", "user", "is_read", "read_date")
    list_filter = ("is_read","read_date")
    search_fields = ("message__text", "user__email")
    
