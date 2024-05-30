from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import *


# Form for the todos
class TodoForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new to-do...'}))

	class Meta:
		model = TodoItem
		fields = '__all__'

# Form to register an user
class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# Form to Login as user
class LoginForm(AuthenticationForm):
	
	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())