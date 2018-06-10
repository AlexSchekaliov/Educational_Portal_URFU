from django.test import TestCase
from educportal.forms import SignUpForm
from educportal.models import User, GroupAccess,AcademicGroup

class SignUpFormTest(TestCase):

    def setUp(self):
        #Создание двух пользователей
        test_user1 = User.objects.create(username='testuser1', email = 'testuser1@mail.ru', password='12345' )
        test_user1.save()
        test_user2 = User.objects.create(username='testuser2', email = 'testuser2@mail.ru',password='1234587')
        test_user2.save()

    def test_first_name_form_date_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['first_name'].label == None or form.fields['first_name'].label == 'Имя')

    def test_last_name_form_date_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['last_name'].label == None or form.fields['last_name'].label == 'Фамилия')

    def test_confirm_password_form_date_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['confirm_password'].label == None or form.fields['confirm_password'].label == 'Подтвердите пароль')

    def test_academic_group_form_date_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['academic_group'].label == None or form.fields['academic_group'].label == 'academic group')

    def test_clean_username_method_false(self):
        # User.objects.create_user(username='testuser1', email='testuser1@mail.ru', password='12345')
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser1' #Пользователь с таким никнеймом уже существует. Форма невалидна
        first_name = 'Тест_3'
        last_name = 'Тест_3'
        email = 'testuser3@email.ru'
        password = 'qwerty'
        confirm_password = 'qwerty'
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertFalse(form.is_valid())

    def test_clean_username_method_true(self):
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser3'
        first_name = 'Тест_3'
        last_name = 'Тест_3'
        email = 'testuser3@email.ru'
        password = 'qwerty'
        confirm_password = 'qwerty'
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertTrue(form.is_valid())


    def test_clean_email_method_true(self):
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser4'
        first_name = 'Тест_4'
        last_name = 'Тест_4'
        email = 'testuser4@email.ru'
        password = 'qwerty'
        confirm_password = 'qwerty'
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertTrue(form.is_valid())


    def test_clean_email_method_false(self):
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser4'
        first_name = 'Тест_4'
        last_name = 'Тест_4'
        email = 'testuser2@mail.ru' #Пользователь с таким email уже существует. Форма невалидна
        password = 'qwerty'
        confirm_password = 'qwerty'
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertFalse(form.is_valid())


    def test_clean_method_false(self):
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser5'
        first_name = 'Тест_5'
        last_name = 'Тест_5'
        email = 'testuser5@mail.ru'
        password = 'qwerty5'
        confirm_password = 'qwerty' # несовпадение паролей. Форма невалидна
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertFalse(form.is_valid())

    def test_clean_method_true(self):
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        username = 'testuser5'
        first_name = 'Тест_5'
        last_name = 'Тест_5'
        email = 'testuser5@mail.ru'
        password = 'qwerty5'
        confirm_password = 'qwerty5'
        academic_group = academic_group.pk
        form_username_field_value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password, 'confirm_password': confirm_password, 'academic_group': academic_group}
        form = SignUpForm(data = form_username_field_value)
        self.assertTrue(form.is_valid())
