from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos, name="home"),
    path("todos/", views.todos, name="Todos")
]