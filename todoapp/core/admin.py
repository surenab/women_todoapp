from django.contrib import admin
from .models import ToDo, ToDoComment
# Register your models here.
admin.site.register(ToDo)
admin.site.register(ToDoComment)
