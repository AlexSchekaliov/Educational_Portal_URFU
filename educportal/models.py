from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    password = forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput(label='Пароль'))
    phone_number = PhoneNumberField(blank = False,null = False)

# Create your models here.
