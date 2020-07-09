from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Restaurant


def home_view(request):
    context = {
        'restaurant_list' : Restaurant.objects.all(),
    }
    return render(request, 'home.html', context)
