from django.shortcuts import redirect, render
from .models import TodoItem
from .forms import *

from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

# Authentication Models and methods
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# def home(request):
#     return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required(login_url="login")
def todos(request):
    items = TodoItem.objects.filter(user=request.user)          # Filtering by user whose is logged in
    form = TodoForm()

    if request.method == 'POST':      

        # for updation and deletion
        todo_id = request.POST.get('todo_id')
        if todo_id:
            todo = TodoItem.objects.get(id=todo_id, user=request.user)      # Ensuring only the user owns the todo

            if 'complete' in request.POST:
                todo.completed = True
            elif 'uncomplete' in request.POST:
                todo.completed = False
            elif 'delete' in request.POST:
                todo.delete()
                return redirect("/")
            
            todo.save()
            return redirect('/')
        
        # for insertion
        form = TodoForm(request.POST)  
        if form.is_valid():
            todo = form.save(commit=False)          # Form has been saved but not in the database so that I can add the user with the todo
            todo.user = request.user                # Associating the todo with the user
            form.save()
        return redirect("/")
    
    return render(request, "todos.html", {"todos": items, 'form': form})

@login_required(login_url="login")
def edit(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id, user=request.user)      # Again ensuring only the user owns the todo
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, "edit.html", {"todo": todo, 'form': form})


def register(request):

	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect("login")
		
	context = {'registerform': form}

	return render(request, 'register.html', context=context)


def login(request):

	form = LoginForm()

	if request.method == "POST":

		form = LoginForm(request, data=request.POST)

		if form.is_valid():
			username =  request.POST.get('username')
			password =  request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("Todos")
	
	context = {'loginform': form}

	return render(request, 'login.html', context=context)


def logout(request):
	auth.logout(request)

	return redirect("/")