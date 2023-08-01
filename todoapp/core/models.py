from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class ToDo(models.Model):

    TODO_TYPES = (
        ("1", "Urgent"),
        ("2", "Regular"),
        ("3", "Low")
    )

    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=60)
    description = models.TextField()
    todo_type = models.CharField(choices=TODO_TYPES, default="2", max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
