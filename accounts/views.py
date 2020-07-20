from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations, Anyad')
            return redirect('blog')
        else:
            import ipdb; ipdb.set_trace()
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            messages.error(request, "Something went wrong")
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})