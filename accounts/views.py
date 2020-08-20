from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # email_subject='Activate your account'
            # email_body='test body'
            # email= EmailMessage(
            #     email_subject,
            #     email_body,
            #     'noreply@givity.com',
            #     [email],
            # )
            # email.send(fail_silently=False)
            user=form.save()
            import ipdb; ipdb.set_trace()
            messages.success(request, 'Registration successful!')
            return redirect('blog')
        else:
            for _, messages_list in form.errors.items():
                for msg in messages_list:
                    messages.error(request, msg)
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})