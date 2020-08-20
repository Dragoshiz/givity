from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, commit=True):
        if not email:
            raise ValueError('Users must have an email adress')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name, 
        )
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password):
        import ipdb; ipdb.set_trace()
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True
    )
    first_name = models.CharField('first name', max_length=100, blank=True)
    last_name = models.CharField('last name', max_length=100, blank=True)

    is_active = models.BooleanField('active', default=False, help_text='Designates whether this user should be treated as active.''Unselect this instead of deleting accounts.')
    is_staff = models.BooleanField('staff status', default=False, help_text='Designates whether the user can log into this admin site.')
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()
    
    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)
        
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True


class ContactPerson(User):
    username = None
    phone = models.CharField(max_length=11)
    CATEGORY_CHOICES = (
        ('MALE', 'Mr.'),
        ('FEMALE', 'Ms.'),
    )
    title = models.CharField(max_length=256, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"