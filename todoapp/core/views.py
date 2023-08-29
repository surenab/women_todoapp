from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import ToDo, ToDoComment
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ToDoForm, ToDoCommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import ToDoFilter
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeDoneView
# Create your views here.


class Base(LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ToDoBase(Base):
    model = ToDo
    form_class = ToDoForm
    success_url = reverse_lazy("my_todos")
    context_object_name = "todo"
    success_text = ""

    def form_valid(self, form):
        messages.success(self.request, self.success_text)
        return super().form_valid(form)


class Home(FilterView):
    context_object_name = "todos"
    filterset_class = ToDoFilter
    template_name = "home.html"
    paginate_by = 2


class CreatToDoComment(CreateView):
    model = ToDoComment
    form_class = ToDoCommentForm
    success_text = "Created!"

    def get_success_url(self) -> str:
        return reverse_lazy("todo_details", kwargs={"pk": self.request.POST.get("todo")})

    def form_valid(self, form):
        form.instance.owner = self.request.user

        messages.success(self.request, "ToDo Comment instance is created!")
        return super().form_valid(form)


class CreatToDo(ToDoBase, CreateView):
    template_name = "create_todo.html"

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(self.request, "ToDo instance is created!")
        return super().form_valid(form)


class MyToDo(ToDoBase, FilterView):
    context_object_name = "todos"
    filterset_class = ToDoFilter
    template_name = "core/todo_list.html"
    paginate_by = 2


class MyToDoDetail(ToDoBase, DetailView):
    pass


class ToDoDetail(DetailView):
    model = ToDo
    context_object_name = "todo"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["comment_form"] = ToDoCommentForm
        data["comments"] = ToDoComment.objects.filter(todo=data["todo"])
        return data


class MyToDoUpdate(ToDoBase, UpdateView):
    success_text = "ToDo instance is updated!"


class MyToDoDelete(ToDoBase, DeleteView):
    success_text = "ToDo instance is deleted!"
