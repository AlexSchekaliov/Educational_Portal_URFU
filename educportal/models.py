from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class SuperSection (models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Название супер раздела")

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = "Супер раздел"
        verbose_name_plural = "Супер разделы"


class GroupAccess(models.Model):
    level_access = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return u"%s" % self.degree

    class Meta:
        verbose_name = "Уровень доступа группы"
        verbose_name_plural = "Уровень доступа групп"


class AcademicGroup(models.Model):

    group_name = models.CharField(max_length=15,unique=True, verbose_name="Название_группы")
    group_access = models.ForeignKey(GroupAccess, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.group_name

    class Meta:
        verbose_name = "Академическая группа"
        verbose_name_plural = "Академические группы"


class Section(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название дисциплины")
    is_guest = models.BooleanField(default=False)
    access_section = models.ForeignKey(GroupAccess, on_delete=models.CASCADE)
    super_section = models.ForeignKey(SuperSection, on_delete=models.CASCADE)

    @property
    def level_access(self):
        return self.access_section.level_access

    def get_absolute_url(self):
        return reverse(
            'theme_list',
            kwargs={
                'supersection_id': self.super_section.pk,
                'section_id': self.pk
            }
        )


    def __str__(self):
        return u"%s" % self.name
    class Meta:

        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

class Theme(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название темы")
    created_date = models.DateTimeField(default=timezone.now)
    discipline = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse(
            'post_list',
            kwargs={
                'supersection_id': self.discipline.super_section.pk,
                'section_id': self.discipline.pk,
                'item_id':self.pk,
            }
        )

    class Meta:
        verbose_name = "Тема дисциплины"
        verbose_name_plural = "Темы дисциплин"

class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Название поста")
    url_to_videopost = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Ссылка на видеоролик", null=True)
    content = models.TextField(null=True, blank=True, verbose_name='Содержимое поста')
    post_type = models.BooleanField(default=True, null=False, verbose_name='Тип поста. 1-пост, 0-видеопост')
    created_date = models.DateTimeField(default=timezone.now)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={
                'supersection_id': self.theme.discipline.super_section.pk,
                'section_id': self.theme.discipline.pk,
                'item_id':self.theme.pk,
                'post_item': self.pk,
            }
        )

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Test(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название теста", null = False)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE, null = False)
    allowable_number_errors = models.PositiveSmallIntegerField(verbose_name='Допустимое количество ошибок', default=1)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse(
            'task_list',
            kwargs={
                'supersection_id': self.theme.discipline.super_section.pk,
                'section_id': self.theme.discipline.pk,
                'item_id':self.theme.pk,
                'test_id':self.pk,
            }
        )

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"



class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок задания", null=False)
    task_content = models.TextField(verbose_name='Текст задания', null=False)
    serial_number = models.PositiveSmallIntegerField(verbose_name='Порядковый номер задания')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


# class Student(models.Model):
#     academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Студент"
#         verbose_name_plural = "Студенты"

# class Department(models.Model):
#     name = models.CharField(max_length=200, verbose_name="Название департамента", null=False)
#
#     def __str__(self):
#         return '%s' % self.name
#
#     class Meta:
#         verbose_name = "Департамент"
#         verbose_name_plural = "Департаменты"

# class Teacher(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
#
#     class Meta:
#         verbose_name = "Преподаватель"
#         verbose_name_plural = "Преподаватели"

class TaskAnswer(models.Model):
    task_answer_content = models.TextField(verbose_name="Текст ответа", null=False)
    is_correct = models.BooleanField(default=False, verbose_name='Корректность ответа')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '%s %d' % (self.task.title, self.pk)

    class Meta:
        verbose_name = "Ответ на задание"
        verbose_name_plural = "Ответы на задания"

class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = PhoneNumberField(verbose_name='Телефон', blank = True,null = True)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, null=True)

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
