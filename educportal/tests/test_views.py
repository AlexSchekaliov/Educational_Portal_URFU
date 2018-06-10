from django.test import TestCase, Client
from django.urls import reverse
from educportal.models import User, GroupAccess, AcademicGroup


class TestViewHomePage(TestCase):

    #Доступность представления по URL - пути

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # Доступность представления по URL - идентификатору
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home_page'))
        self.assertEqual(resp.status_code, 200)

    # Проверка на использование представлением корректного шаблона
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'educportal/home_page.html')


class LoginViewHomePage(TestCase):

    # Доступность представления по URL - пути
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    # Доступность представления по URL - идентификатору
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('login_page'))
        self.assertEqual(resp.status_code, 200)

    # Проверка на использование представлением корректного шаблона
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('login_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'educportal/login.html')



class ProfilePageViewTest(TestCase):

    def setUp(self):
    #Создание пользователz и сохранение их в тестовой базе данных
        group_access_obj = GroupAccess.objects.create(level_access=2, degree='Магистр')
        academic_group = AcademicGroup.objects.create(group_name='МТ-1', group_access=group_access_obj)
        test_user1 = User.objects.create(username='testuser1', first_name='Тест_1', last_name='Тест_1', email = 'testuser1@mail.ru', academic_group=academic_group)
        test_user1.set_password('12345')
        test_user1.save()

    # Пользователь является анонимным
    # Доступность представления по URL - пути
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/profile/')
        self.assertEqual(resp.status_code, 302)

    # Доступность представления по URL - идентификатору
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('profile_page'))
        self.assertEqual(resp.status_code, 302)

    # Проверка на использование представлением корректного шаблона
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('profile_page'))
        self.assertEqual(resp.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('profile_page'))
        self.assertRedirects(resp, '/login/?next=/profile/')


    # Пользователь авторизовался
    def test_view_url_exists_at_desired_location_loggin_in(self):
        self.client.login(username='testuser1', password='12345') #авторизация пользователя
        resp = self.client.get('/profile/')
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)

    # Доступность представления по URL - идентификатору
    def test_view_url_accessible_by_name_loggin_in(self):
        self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('profile_page'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)


    # Проверка на использование представлением корректного шаблона

    def test_view_uses_correct_template_loggin_in(self):
        self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('profile_page'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'educportal/profile_page.html')



