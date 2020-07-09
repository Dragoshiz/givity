from django.contrib import admin

# Register your models here.
from .models import Restaurant, Musician, Florist
# from .models import Dancers

admin.site.register(Restaurant)

admin.site.register(Musician)

admin.site.register(Florist)

# admin.site.register(Dancers)