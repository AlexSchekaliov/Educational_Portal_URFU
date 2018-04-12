from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField


class StudentGroupAccess(models.Model):
    level_access = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return u"%s" % self.degree

    class Meta:
        verbose_name = "Уровень доступа группы"
        verbose_name_plural = "Уровень доступа групп"


class AcademicGroup(models.Model):

    group_name = models.CharField(max_length=15,unique=True, verbose_name="Название_группы")
    group_access = models.ForeignKey(StudentGroupAccess, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.group_name

    class Meta:
        verbose_name = "Академическая группа"
        verbose_name_plural = "Академические группы"


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = PhoneNumberField(verbose_name='Телефон', blank = False,null = False)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, null = True)

# Create your models here.
