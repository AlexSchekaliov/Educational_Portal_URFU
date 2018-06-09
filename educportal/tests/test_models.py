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
        group_acc_obj = GroupAccess.objects.get(id=2)
        field_label = group_acc_obj._meta.get_field('level_access').verbose_name
        self.assertEquals(field_label, 'level access')

    def test_Level_access_label_name_false(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
        field_label = group_acc_obj._meta.get_field('level_access').verbose_name
        self.assertNotEquals(field_label, 'kasuchgisa')

    def test_degree_label_name(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
        field_label = group_acc_obj._meta.get_field('degree').verbose_name
        self.assertEquals(field_label, 'degree')

    def test_degree_label_name_false(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
        field_label = group_acc_obj._meta.get_field('degree').verbose_name
        self.assertNotEquals(field_label, 'lkcquscc')

    def test_degree_max_length(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
        max_length = group_acc_obj._meta.get_field('degree').max_length
        self.assertEquals(max_length, 10)

    def test_degree_max_length_false(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
        max_length = group_acc_obj._meta.get_field('degree').max_length
        self.assertNotEquals(max_length, 20)

    def test_str_method(self):
        group_acc_obj = GroupAccess.objects.get(id=2)
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


