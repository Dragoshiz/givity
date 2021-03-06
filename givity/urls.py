"""givity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from services.views import blog_view, detail_view
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('admin/', admin.site.urls),
    path('home/', include('services.urls')),
    path('register/', register, name='register'),
    
    path('', blog_view, name='blog'),
    path('<int:id>/', detail_view, name='detail'),
    
    path('password_reset/',
     auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
     name='reset_password'),

    path('password_reset_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
     name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
     name='password_reset_confirm'),
    
    path('password_reset_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
     name='password_reset_complete'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
