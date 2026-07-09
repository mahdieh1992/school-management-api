from django.contrib import admin
from .models import School, Lesson, ClassRoom
from ..news.admin import NewsInline
# Register your models here.

class ClassRoomInline(admin.StackedInline):
   model = ClassRoom
   extra = 0

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
   """
    Admin configuration for the School model.
   """
   list_display = ("name", "latitude", "longitude","created_at", "updated_at")
   search_fields = ("name",)
   ordering = ("name",)
   inlines = [ClassRoomInline,]
   
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
   """
      Admin configuration for the Lesson model.
   """
   list_display = ("title", "code","created_at", "updated_at")
   ordering = ("code",)
   search_fields = ("title", "code")
   list_editable = ("code",)
   inlines = [ClassRoomInline,]
   
@admin.register(ClassRoom)  
class ClassRoomAdmin(admin.ModelAdmin):
   """
      Admin configuration for the ClassRoom model.
   """
   list_display = ("name", "school", "lesson", "teacher","created_at", "updated_at")
   search_fields = ("name", "school__name")
   list_filter = ("school", "lesson")
   inlines = [NewsInline]
   