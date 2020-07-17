from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantImage, Musician, MusicianImage
from .models import Florist, FloristImage, Dancer, DancerImage


class RestaurantImageAdmin(admin.StackedInline):
    model = RestaurantImage


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [RestaurantImageAdmin]


admin.site.register(Restaurant, RestaurantAdmin)


class MusicianImageAdmin(admin.StackedInline):
    model = MusicianImage


class MusicianAdmin(admin.ModelAdmin):
    inlines = [MusicianImageAdmin]


admin.site.register(Musician, MusicianAdmin)


class FloristImageAdmin(admin.StackedInline):
    model = FloristImage


class FloristAdmin(admin.ModelAdmin):
    inlines = [FloristImageAdmin]


admin.site.register(Florist, FloristAdmin)


class DancerImageAdmin(admin.StackedInline):
    model = DancerImage


class DancerAdmin(admin.ModelAdmin):
    inlines = [DancerImageAdmin] 


admin.site.register(Dancer, DancerAdmin)