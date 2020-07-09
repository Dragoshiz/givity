from django.db import models


# Create your models here.

class ContactPerson(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    phone = models.CharField(max_length=11)
    CATEGORY_CHOICES = (
        ('MALE', 'Mr.'),
        ('FEMALE', 'Ms.'),
    )
    title = models.CharField(max_length=256, choices=CATEGORY_CHOICES)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    