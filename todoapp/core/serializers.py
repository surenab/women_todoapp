from rest_framework import serializers
from .models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["id", "start_date", "end_date", "title", "description", "todo_type", "user", "active", "tags"]
