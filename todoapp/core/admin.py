from django.contrib import admin
from .models import ToDo, ToDoComment, Tag
# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "start_date", "end_date", "title", "description", "todo_type", "user", "active")
    list_filter = ("start_date", "end_date", "user")
    search_fields = ("title", "description")
    filter_horizontal = ("tags",)


admin.site.register(ToDo, ToDoAdmin)

admin.site.register(ToDoComment)
admin.site.register(Tag)
