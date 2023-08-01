from django.urls import path, include
from .views import home, CreatToDo

urlpatterns = [
    path("", home, name="home"),
    path("create-todo", CreatToDo.as_view(), name="create_todo"),
]
