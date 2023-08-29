from django.urls import path, include
from .views import Home, CreatToDo, MyToDo, MyToDoDetail, MyToDoUpdate, MyToDoDelete, CreatToDoComment, ToDoDetail

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("my-todos", MyToDo.as_view(), name="my_todos"),
    path("my-todos/details/<int:pk>", MyToDoDetail.as_view(), name="my_todo_details"),
    path("details/<int:pk>", ToDoDetail.as_view(), name="todo_details"),
    path("my-todos/update/<int:pk>", MyToDoUpdate.as_view(), name="my_todo_update"),
    path("my-todos/delete/<int:pk>", MyToDoDelete.as_view(), name="my_todo_delete"),
    path("create-todo", CreatToDo.as_view(), name="create_todo"),
    path("create-comment", CreatToDoComment.as_view(), name="create_comment"),
]
