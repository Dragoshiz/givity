from django.db import models


# Create your models here.
class ContactPerson(models.Model):
    first_name = models.CharField('First Name', max_length=256)
