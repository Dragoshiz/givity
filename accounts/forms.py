from django import forms
from .models import ContactPerson, User    
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ContactPerson
        fields = ['first_name', 'last_name', 'email', 'phone', 'title']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email_exists = User.objects.filter(email=cleaned_data['email']).exists()
        if email_exists:
            raise forms.ValidationError("Email already exists, anyad!")
        return cleaned_data
