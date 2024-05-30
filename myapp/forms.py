from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import *


# Form for the todos
class TodoForm(forms.ModelForm):
	title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add new to-do...'
        })
    )
	class Meta:
		model = TodoItem
		fields = ['title', 'completed']  # Excluded the user as it will be auto generated

# Form to register an user
class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter username'
        })
		self.fields['email'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter email'
        })
		self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter password'
        })
		self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirm password'
        })


# Form to Login as user
class LoginForm(AuthenticationForm):
	
	username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter username'
    }))
	password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter password'
    }))