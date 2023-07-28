from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.http import HttpResponse
# Create your views here.


class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


def home(request):
    return HttpResponse(f"home page for {request.user.email}")


def home2(request):
    return HttpResponse("home page aftre logout: NO user info")
