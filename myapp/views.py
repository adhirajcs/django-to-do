from django.shortcuts import redirect, render, HttpResponse
from .models import TodoItem
from .forms import *

# Create your views here.

# def home(request):
#     return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def todos(request):
    items = TodoItem.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)        
        if form.is_valid():
            form.save()
        return redirect("/")

    return render(request, "todos.html", {"todos": items ,'form':form})


# def todos(request):
#     items = TodoItem.objects.all()
#     form = TodoForm()
#     if request.method == 'POST':
#         # new_todo_title = TodoForm(request.POST)
#         if new_todo_title:
#             # new_todo = TodoItem.objects.create(title=new_todo_title, completed=False)
#             new_todo_title.save()
#             redirect("/")
    # return render(request, "todos.html", {"todos": items ,'form':form})
