from django import forms
from .models import ContactPerson    
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ContactPerson
        fields = ['first_name', 'last_name', 'email', 'phone', 'title']
