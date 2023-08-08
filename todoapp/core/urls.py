from django.urls import path, include
from .views import home, CreatToDo, MyToDo, MyToDoDetail, MyToDoUpdate, MyToDoDelete

urlpatterns = [
    path("", home, name="home"),
    path("my-todos", MyToDo.as_view(), name="my_todos"),
    path("my-todos/details/<int:pk>", MyToDoDetail.as_view(), name="my_todo_details"),
    path("my-todos/update/<int:pk>", MyToDoUpdate.as_view(), name="my_todo_update"),
    path("my-todos/delete/<int:pk>", MyToDoDelete.as_view(), name="my_todo_delete"),
    path("create-todo", CreatToDo.as_view(), name="create_todo"),
]
