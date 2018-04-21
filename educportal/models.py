from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField


class StudentGroupAccess(models.Model):
    level_access = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=10, blank=False, null=False, unique=True)

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


class Discipline(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название дисциплины")
    for_super_section = models.ForeignKey(StudentGroupAccess, on_delete=models.CASCADE,null = True)

    def __str__(self):
        return u"%s" % self.name
    class Meta:

        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

class ThemeDiscipline(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название темы")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Тема дисциплины"
        verbose_name_plural = "Темы дисциплин"

class VideoPost(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название видеопоста")
    link_to_youtube = models.CharField(max_length=200, unique= True, verbose_name="Ссылка на youtube")
    theme = models.ForeignKey(ThemeDiscipline, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Видеопост"
        verbose_name_plural = "Видеопосты"




class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = PhoneNumberField(verbose_name='Телефон', blank = True,null = True)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)

    @property
    def level_access(self):
        return self.academic_group.group_access.level_access

    @property
    def degree_student(self):
        return self.academic_group.group_access.degree

# Create your models here.
