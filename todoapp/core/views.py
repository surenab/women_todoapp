from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
from django.views.generic import CreateView
from .forms import ToDoForm
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    todos = ToDo.objects.all()
    return render(request=request, template_name="home.html", context={"todos": todos})


class CreatToDo(CreateView):
    form_class = ToDoForm
    success_url = reverse_lazy("home")
    template_name = "create_todo.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
