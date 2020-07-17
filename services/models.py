from django.db import models
from accounts.models import User


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField('Description', max_length=1024)
    price_range = models.IntegerField(default=0)
    rating = models.IntegerField('customer rating')
    main_image = models.ImageField(default=None, upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Restaurant(Services):
    cuisine = models.TextField('type of food')
    max_seats = models.PositiveIntegerField('Seats available')
    ballroom = models.BooleanField('Has wedding ballroom')
    is_chain = models.BooleanField()
    has_food_sample = models.BooleanField()
    has_parking = models.BooleanField('Restaurant parking')
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)


class RestaurantImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    restaurant = models.ForeignKey(Restaurant, default=None, on_delete=models.CASCADE)   
    
    
class Musician(Services):
    MUSICIAN_CATEGORY = [
        ('BAND', 'Band'),
        ('DJ', 'Dj'),
        ('SINGER', 'Singer'),
        ('ORCHESTRA', 'Orchestra'),
        ('PIANIST', 'Pianist'),
        ('VIOLONIST', 'Violonist'),
        ('PERCUSSIONIST', 'Percussionist'),
        ('OTHER', 'Other')
    ]
    musician = models.CharField(max_length=512, choices=MUSICIAN_CATEGORY)

    GEN_CHOICES = [
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('HIP HOP', 'Hip hop'),
        ('MANELE', 'Manele'),
        ('EDM', 'EDM'),
        ('CLASSICAL', 'Classical'),
        ('BLUES', 'Blues'),
        ('JAZZ', 'Jazz'),
        ('RNB', 'RnB'),
        ('FOLK', 'Folk'),
        ('INDIE', 'Indie'),
        ('OTHER', 'Other'),
    ]
    genre = models.CharField(max_length=512, choices=GEN_CHOICES)
    musician_num = models.IntegerField('Number of musicians', default=1)
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)


class MusicianImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    musician = models.ForeignKey(Musician, default=None, on_delete=models.CASCADE)


class Florist(Services):
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)


class FloristImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    florist = models.ForeignKey(Florist, default=None, on_delete=models.CASCADE)
    


class Dancer(Services):
    DANCE_CHOICES = [
        ('BALLET', 'Ballet'),
        ('TAP', 'Tap'),
        ('JAZZ', 'Jazz'),
        ('MODERN', 'Modern'),
        ('LYRICAL', 'Lyrical'),
        ('HIP_HOP', 'Hip Hop'),
        ('CONTEMPORARY', 'Contemporary'),
        ('FOLK', 'Folk'),
    ]
    dance_type = models.TextField(choices=DANCE_CHOICES)
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)


class DancerImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    dancer = models.ForeignKey(Dancer, default=None, on_delete=models.CASCADE)
