from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Restaurant, RestaurantImage


def home_view(request):
    context = {
        'restaurant_list': Restaurant.objects.all(),
    }
    return render(request, 'home.html', context)


def blog_view(request):
    posts = Restaurant.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def detail_view(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    photos = RestaurantImage.objects.filter(restaurant=restaurant)
    return render(request, 'detail.html', {
        'post': restaurant,
        'photos': photos
    })