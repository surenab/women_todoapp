from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name


class ToDo(models.Model):

    TODO_TYPES = (
        ("1", "Urgent"),
        ("2", "Regular"),
        ("3", "Low")
    )

    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    todo_type = models.CharField(choices=TODO_TYPES, default="2", max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title} {self.description}"


class ToDoComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

    def __str__(self) -> str:
        return f"{self.owner.username} is commneted {self.text}"
