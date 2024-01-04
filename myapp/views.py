from django.shortcuts import redirect, render, HttpResponse
from .models import TodoItem

# Create your views here.

def home(request):
    return render(request, "home.html")

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request, "todos.html", {"todos": items })

def todos(request):
    items = TodoItem.objects.all()
    if request.method == 'POST':
        new_todo_title = request.POST.get('newTodo')
        if new_todo_title:
            new_todo = TodoItem.objects.create(title=new_todo_title, completed=False)
            new_todo.save()
            redirect("todos.html")
    return render(request, "todos.html", {"todos": items })

# def add_todos(request):
#     if request.method == 'POST':
#         new_todo_title = request.POST.get('newTodo')
#         if new_todo_title:
#             new_todo = TodoItem.objects.create(title=new_todo_title, completed=False)
#             new_todo.save()
#             redirect("todos.html")