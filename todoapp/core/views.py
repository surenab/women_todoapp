from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ToDoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def home(request):
    todos = ToDo.objects.all()
    return render(request=request, template_name="home.html", context={"todos": todos})


class CreatToDo(LoginRequiredMixin, CreateView):
    form_class = ToDoForm
    success_url = reverse_lazy("my_todos")
    template_name = "create_todo.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "ToDo instance is created!")
        return super().form_valid(form)


class MyToDo(LoginRequiredMixin, ListView):
    model = ToDo

    context_object_name = "todos"

    def get_queryset(self):
        queryset = super(MyToDo, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MyToDoDetail(LoginRequiredMixin, DetailView):
    model = ToDo
    context_object_name = "todo"

    def get_queryset(self):
        queryset = super(MyToDoDetail, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MyToDoUpdate(LoginRequiredMixin, UpdateView):
    model = ToDo
    context_object_name = "todo"
    form_class = ToDoForm
    success_url = reverse_lazy("my_todos")

    def get_queryset(self):
        queryset = super(MyToDoUpdate, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "ToDo instance is updated!")
        return super().form_valid(form)


class MyToDoDelete(LoginRequiredMixin, DeleteView):
    model = ToDo
    context_object_name = "todo"
    success_url = reverse_lazy("my_todos")

    def get_queryset(self):
        queryset = super(MyToDoDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.info(self.request, "ToDo instance is deleted!")
        return super().form_valid(form)
