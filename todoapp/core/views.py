from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ToDoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import ToDoFilter
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


class MyToDoUpdate(ToDoBase, UpdateView):
    success_text = "ToDo instance is updated!"


class MyToDoDelete(ToDoBase, DeleteView):
    success_text = "ToDo instance is deleted!"
