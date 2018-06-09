from django.test import TestCase
from educportal.models import *

class SuperSectionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        SuperSection.objects.create(name='Бакалаврам')

    def test_first_name_label(self):
        super_section=SuperSection.objects.get(id=1)
        field_label = super_section._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название супер раздела')

    def test_first_name_label_false(self):
        super_section=SuperSection.objects.get(id=1)
        field_label = super_section._meta.get_field('name').verbose_name
        self.assertNotEquals(field_label,'Некорректное название раздела')

    def test_name_max_length_true(self):
        super_section = SuperSection.objects.get(id=1)
        max_length = super_section._meta.get_field('name').max_length
        self.assertEquals(max_length, 10)

    def test_name_max_length_false(self):
        super_section = SuperSection.objects.get(id=1)
        max_length = super_section._meta.get_field('name').max_length
        self.assertNotEquals(max_length, 15)

    def test_str_method(self):
        super_section = SuperSection.objects.get(id=1)
        expected_super_section_name = '%s' % super_section.name
        self.assertEquals(expected_super_section_name, str(super_section))


class GroupAccessModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        groupAccess = GroupAccess.objects.create(level_access=2,degree='Магистр')

    def test_Level_access_label_name(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        field_label = group_acc_obj._meta.get_field('level_access').verbose_name
        self.assertEquals(field_label, 'level access')

    def test_Level_access_label_name_false(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        field_label = group_acc_obj._meta.get_field('level_access').verbose_name
        self.assertNotEquals(field_label, 'kasuchgisa')

    def test_degree_label_name(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        field_label = group_acc_obj._meta.get_field('degree').verbose_name
        self.assertEquals(field_label, 'degree')

    def test_degree_label_name_false(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        field_label = group_acc_obj._meta.get_field('degree').verbose_name
        self.assertNotEquals(field_label, 'lkcquscc')

    def test_degree_max_length(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        max_length = group_acc_obj._meta.get_field('degree').max_length
        self.assertEquals(max_length, 10)

    def test_degree_max_length_false(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        max_length = group_acc_obj._meta.get_field('degree').max_length
        self.assertNotEquals(max_length, 20)

    def test_str_method(self):
        group_acc_obj = GroupAccess.objects.get(id=1)
        expected_group_acc_degree = '%s' % group_acc_obj.degree
        self.assertEquals(expected_group_acc_degree, str(group_acc_obj))



class AcademicGroupModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        group_access_obj=GroupAccess.objects.create(level_access=2,degree='Магистр')
        AcademicGroup.objects.create(group_name = 'МТ-1', group_access=group_access_obj)

    def test_group_name_label(self):
        academ_group_obj=AcademicGroup.objects.get(id=1)
        field_label = academ_group_obj._meta.get_field('group_name').verbose_name
        self.assertEquals(field_label,'Название_группы')

    def test_group_name_label_false(self):
        academ_group_obj=AcademicGroup.objects.get(id=1)
        field_label = academ_group_obj._meta.get_field('group_name').verbose_name
        self.assertNotEquals(field_label,'Название_музыкальной_группы')

    def test_group_name_max_length(self):
        academ_group_obj = AcademicGroup.objects.get(id=1)
        max_length = academ_group_obj._meta.get_field('group_name').max_length
        self.assertEquals(max_length, 15)


    def test_group_name_max_length_false(self):
        academ_group_obj = AcademicGroup.objects.get(id=1)
        max_length = academ_group_obj._meta.get_field('group_name').max_length
        self.assertNotEquals(max_length, 5)

    def test_str_method(self):
        academ_group_obj = AcademicGroup.objects.get(id=1)
        expected_academ_group_obj_name = '%s' % academ_group_obj.group_name
        self.assertEquals(expected_academ_group_obj_name, str(academ_group_obj))




class SectionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        access_section = GroupAccess.objects.create(level_access=1,degree='Бакалавр')
        super_section = SuperSection.objects.create(name='Бакалаврам')
        Section.objects.create(name = 'Компьютерные сети',is_guest=False, access_section=access_section, super_section=super_section)


    def test_name_label(self):
        section_obj = Section.objects.get(id=1)
        field_label = section_obj._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название дисциплины')

    def test_name_label_false(self):
        section_obj = Section.objects.get(id=1)
        field_label = section_obj._meta.get_field('name').verbose_name
        self.assertNotEquals(field_label,'Название макарон')

    def test_level_access_property(self):
        section_obj = Section.objects.get(id=1)

        self.assertEquals( section_obj.level_access, section_obj.access_section.level_access)

    def test_get_absolute_url(self):
        section_obj = Section.objects.get(id=1)

        self.assertEquals(section_obj.get_absolute_url(), '/degrees/1/1/themes')

    def test_str_method(self):
        section_obj = Section.objects.get(id=1)
        expected_section_obj_name = '%s' % section_obj.name
        self.assertEquals(expected_section_obj_name, str(section_obj))


    def test_get_absolute_url_false(self):
        section_obj = Section.objects.get(id=1)
        self.assertNotEquals(section_obj.get_absolute_url(), '/degrees/3/4/themes')


class ThemeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        access_section = GroupAccess.objects.create(level_access=3, degree='Аспирант')
        super_section = SuperSection.objects.create(name='Аспирантам')
        discipline = Section.objects.create(name='Глубокие нейронные сети',is_guest=True, access_section=access_section, super_section=super_section)
        Theme.objects.create(name = 'Тема_1', created_date=timezone.now(),discipline=discipline)


    def test_name_label(self):
        theme_obj = Theme.objects.get(id=1)
        field_label = theme_obj._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название темы')

    def test_name_label_false(self):
        theme_obj = Theme.objects.get(id=1)
        field_label = theme_obj._meta.get_field('name').verbose_name
        self.assertNotEquals(field_label,'Название суперраздела')


    def test_get_absolute_url(self):

        theme_obj = Theme.objects.get(id=1)
        self.assertEquals(theme_obj.get_absolute_url(), '/degrees/1/1/themes/1/post/')


    def test_get_absolute_url_false(self):

        theme_obj = Theme.objects.get(id=1)

        self.assertNotEquals(theme_obj.get_absolute_url(), '/degrees/5/3/themes/1/post/')

    def test_str_method(self):
        theme_obj = Theme.objects.get(id=1)
        expected_theme_obj_name = '%s' % theme_obj.name
        self.assertEquals(expected_theme_obj_name, str(theme_obj))



class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        access_section = GroupAccess.objects.create(level_access=3, degree='Аспирант')
        super_section = SuperSection.objects.create(name='Аспирантам')
        discipline = Section.objects.create(name='Глубокие нейронные сети',is_guest=True, access_section=access_section, super_section=super_section)
        theme = Theme.objects.create(name = 'Тема_1', created_date=timezone.now(),discipline=discipline)
        Post.objects.create(title='Название_поста_1', url_to_videopost = 'https://www.youtube.com/embed/kuEnh_uqehA', post_type=False, theme = theme)


    def test_title_label(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Название поста')

    def test_name_label_false(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('title').verbose_name
        self.assertNotEquals(field_label,'Название название')

    def test_title_url_to_videopost(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('url_to_videopost').verbose_name
        self.assertEquals(field_label,'Ссылка на видеоролик')

    def test_name_label_url_to_videopost(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('url_to_videopost').verbose_name
        self.assertNotEquals(field_label,'Ссылка на аудиоролик')


    def test_title_max_length(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('title').max_length
        self.assertEquals(field_label, 200)

    def test_title_max_length_false(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('title').max_length
        self.assertNotEquals(field_label,150)

    def test_url_to_videopost_max_length(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('url_to_videopost').max_length
        self.assertEquals(field_label,200)

    def test_url_to_videopost_max_length_false(self):
        post_obj = Post.objects.get(id=1)
        field_label = post_obj._meta.get_field('url_to_videopost').max_length
        self.assertNotEquals(field_label,15)


    def test_get_absolute_url(self):

        post_obj = Post.objects.get(id=1)
        self.assertEquals(post_obj.get_absolute_url(), '/degrees/1/1/themes/1/post/1')

    def test_get_absolute_url_false(self):

        post_obj = Post.objects.get(id=1)
        self.assertNotEquals(post_obj.get_absolute_url(), '/degrees/1/1/themes/14/posвыt/1')


    def test_str_method(self):
        post_obj = Post.objects.get(id=1)
        expected_post_obj_name = '%s' % post_obj.title
        self.assertEquals(expected_post_obj_name, str(post_obj))

class TestModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        access_section = GroupAccess.objects.create(level_access=3, degree='Аспирант')
        super_section = SuperSection.objects.create(name='Аспирантам')
        discipline = Section.objects.create(name='Глубокие нейронные сети', is_guest=True,
                                            access_section=access_section, super_section=super_section)
        theme = Theme.objects.create(name='Тема_1', created_date=timezone.now(), discipline=discipline)
        Test.objects.create(name='Тест_1', theme=theme, allowable_number_errors=2)

    def test_get_absolute_url(self):
        test_obj = Test.objects.get(id=1)
        self.assertEquals(test_obj.get_absolute_url(), '/degrees/1/1/themes/1/test/1')

    def test_get_absolute_url_false(self):
        test_obj = Test.objects.get(id=1)
        self.assertNotEquals(test_obj.get_absolute_url(), '/degrees/1/1/themes/14/post/1')

    def test_str_method(self):
        test_obj = Test.objects.get(id=1)
        expected_test_obj_name = '%s' % test_obj.name
        self.assertEquals(expected_test_obj_name, str(test_obj))


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        access_section = GroupAccess.objects.create(level_access=3, degree='Аспирант')
        academic_group=AcademicGroup.objects.create(group_name='КН-3', group_access=access_section)
        User.objects.create(username = 'Test', first_name='Тест', last_name='Тест', password='Test', email='test@test.ru', academic_group=academic_group)

    def test_academ_group_student_ptoperty(self):
        user_obj = User.objects.get(id=1)
        self.assertEquals(user_obj.academ_group_student, user_obj.academic_group.group_name)

    def test_degree_student(self):
        user_obj = User.objects.get(id=1)
        self.assertEquals(user_obj.degree_student, user_obj.academic_group.group_access.degree)

    def test_level_access(self):
        user_obj = User.objects.get(id=1)
        self.assertEquals(user_obj.level_access, user_obj.academic_group.group_access.level_access)

