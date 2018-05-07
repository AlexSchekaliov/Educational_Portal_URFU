from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class SuperSection (models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Название супер раздела")

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Супер раздел"
        verbose_name_plural = "Супер разделы"


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


class Section(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название дисциплины")
    is_guest = models.BooleanField(default=False)
    access_section = models.ForeignKey(StudentGroupAccess, on_delete=models.CASCADE,null = True)
    super_section = models.ForeignKey(SuperSection, on_delete=models.CASCADE, null= True)


    def __str__(self):
        return u"%s" % self.name
    class Meta:

        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

class Theme(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название темы")
    discipline = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Тема дисциплины"
        verbose_name_plural = "Темы дисциплин"

class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Название поста", null=False)
    url_to_videopost = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Ссылка на видеоролик", null=True)
    content = models.TextField(null=True, blank=True, verbose_name='Содержимое поста')
    post_type = models.BooleanField(default=True, null=False, verbose_name='Тип поста. 1-пост, 0-видеопост')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"




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

    @property
    def academ_group_student(self):
        return self.academic_group.group_name

# Create your models here.
