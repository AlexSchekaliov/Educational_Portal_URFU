from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = PhoneNumberField(blank = False,null = False)

# Create your models here.