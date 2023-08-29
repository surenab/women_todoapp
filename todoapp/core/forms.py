from typing import Any
from django import forms
from .models import ToDo, ToDoComment


class ToDoForm(forms.ModelForm):
    TODO_TYPES = (
        ("1", "Urgent"),
        ("2", "Regular"),
        ("3", "Low")
    )

    todo_type = forms.ChoiceField(choices=TODO_TYPES)
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = ToDo
        fields = ["start_date", "end_date", "title", "description", "todo_type"]


class ToDoCommentForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = ToDoComment
        fields = ["text", "todo"]
