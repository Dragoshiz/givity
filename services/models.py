from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField('Name of Restaurant', max_length=512)