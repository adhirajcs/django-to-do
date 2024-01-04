from django.urls import path
from . import views

urlpatterns = [
    # path("", views.todos, name="home"),
    path("", views.todos, name="Todos")
]