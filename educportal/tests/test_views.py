from django.test import TestCase
from django.urls import reverse
from educportal.models import User, GroupAccess, AcademicGroup,SuperSection,Section,Theme,Post


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



class SectionListView(TestCase):

    def setUp(self):

        # Создание суперразделов (разделов главного навигационного меню)

        # Создание динамического раздела "Бакалаврам"

            self.bachalor_section = SuperSection.objects.create(name="Бакалаврам")
            self.master_section = SuperSection.objects.create(name="Магистрам")
            list_super_section = {self.bachalor_section, self.master_section}
            # Сохрание в  тестовой базе данныъ созданныъ разделов
            for list_super_section_item in list_super_section:
                list_super_section_item.save()


        # Создание экземпляров модели GroupAccess, содержащей информацию о уровне доступа объектов веб-портала.

            group_access_bachalor = GroupAccess.objects.create(level_access=1, degree='Бакалавр')
            group_access_master = GroupAccess.objects.create(level_access=2, degree='Магистр')
        # Сохрание в  тестовой базе данныъ созданныъ экземпляров модели GroupAccess
            list_group_sccess = {group_access_bachalor, group_access_master}
            for list_group_sccess_item in list_group_sccess:
                list_group_sccess_item.save()

        # Создание 30 тестовых разделов-дисциплин

            number_of_disciplines = 30
            for disciplite_section in range(number_of_disciplines):
                if disciplite_section % 2:
                    access_section = group_access_master
                    is_guest = True
                    super_section = self.master_section
                else:
                    access_section = group_access_bachalor
                    is_guest = False
                    super_section = self.bachalor_section

                section_item = Section.objects.create(name='Дисциплина %s'% disciplite_section, access_section=access_section, is_guest=is_guest, super_section=super_section)
                section_item.save()

        # Проверка валидности url.
    def test_view_valid_url(self):

        resp = self.client.get(reverse('section_page', args=[self.bachalor_section.pk, ]))
        self.assertEqual(resp.status_code, 200)


        # Проверка на использование представлением корректного шаблона
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('section_page', args=[self.master_section.pk, ]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'educportal/section_list.html')


    # Проверка длины содержимого переменной section для раздела "Бакалаврам"
    def test_context_section_length_bachalor(self):
        resp = self.client.get(reverse('section_page', args=[self.bachalor_section.pk, ]))
        self.assertTrue('section' in resp.context)
        self.assertEqual(len(resp.context['section']), 15)

    # Проверка длины содержимого переменной section_guest для раздела "Бакалаврам"
    def test_context_section_guest_length_bachalor(self):
        resp = self.client.get(reverse('section_page', args=[self.bachalor_section.pk, ]))
        self.assertTrue('section_guest' in resp.context)
        self.assertEqual(len(resp.context['section_guest']), 0)

    # Проверка длины содержимого переменной section для раздела "Магистрам"
    def test_context_section_length_master(self):
        resp = self.client.get(reverse('section_page', args=[self.master_section.pk, ]))
        self.assertTrue('section' in resp.context)
        self.assertEqual(len(resp.context['section']), 0)

    # Проверка длины содержимого переменной section_guest для раздела "Магистрам"
    def test_context_section_guest_length_master(self):
        resp = self.client.get(reverse('section_page', args=[self.master_section.pk, ]))
        self.assertTrue('section_guest' in resp.context)
        self.assertEqual(len(resp.context['section_guest']), 15)


class TestPostDetailView(TestCase):

    def setUp(self):

        # Создание экземпляров модели GroupAccess, содержащей информацию о уровне доступа объектов веб-портала.
        group_access_bachalor = GroupAccess.objects.create(level_access=1, degree='Бакалавр')
        group_access_master = GroupAccess.objects.create(level_access=2, degree='Магистр')

        # Создание академических групп

        academic_group_bachalor = AcademicGroup.objects.create(group_name='МТ-1', group_access= group_access_bachalor)
        academic_group_master = AcademicGroup.objects.create(group_name='МГПИ-1',group_access= group_access_master)


        # Создание 2-х пользователей: Бакалавр и магистр

        test_user1 = User.objects.create(username='testuser1', email='testuser1@mail.ru', academic_group = academic_group_bachalor)
        test_user1.set_password('12345')
        test_user1.save()
        test_user2 = User.objects.create(username='testuser2', email='testuser2@mail.ru', academic_group = academic_group_master)
        test_user2.set_password('1234587')
        test_user2.save()

        # Создание суперразделов (разделов главного навигационного меню)

        self.bachalor_section = SuperSection.objects.create(name="Бакалаврам")
        self.master_section = SuperSection.objects.create(name="Магистрам")

        # Создание 2 тестовых разделов-дисциплин

        self.discipline_bachalor_section = Section.objects.create(name='Дисциплина_1', access_section= group_access_bachalor, super_section=self.bachalor_section)
        self.discipline_master_section = Section.objects.create(name='Дисциплина_2', access_section= group_access_master,super_section=self.master_section)

        # Создание 2  тем, ассоциированных с разделами-дисциплинами

        self.theme_for_discipline_bachalor_section = Theme.objects.create(name='Тема_1',discipline=self.discipline_bachalor_section)
        self.theme_for_discipline_master_section = Theme.objects.create(name='Тема_1',discipline=self.discipline_master_section)

        # Создание 2 поста, ассоцированных с конкретной темой.

        self.first_post = Post.objects.create(title='Пост_1', theme=self.theme_for_discipline_bachalor_section)
        self.second_post = Post.objects.create(title='Пост_2', theme=self.theme_for_discipline_master_section)




        # Проверка  механизма контроля доступа.
    def test_access_to_post_anonymous_user(self): # Анонимный пользователь

        resp_bachalor = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.bachalor_section.pk,
                                                                'section_id': self.discipline_bachalor_section.pk,
                                                                'item_id':self.theme_for_discipline_bachalor_section.pk,
                                                                'post_item': self.first_post.pk,}))

        resp_master = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.master_section.pk,
                                                                       'section_id': self.discipline_master_section.pk,
                                                                       'item_id': self.theme_for_discipline_master_section.pk,
                                                                       'post_item': self.second_post.pk, }))

        self.assertEqual(resp_bachalor.status_code, 403) # Нет прав доступа к приватной ветке "Бакалаврам"
        self.assertEqual(resp_master.status_code, 403)  # Нет прав доступа к приватной ветке "Магистрам"


    def test_access_to_post_bachalor_user(self): # пользователь с правами "Бакалавр"

        self.client.login(username='testuser1', password='12345') # Регистрируем пользователя с правами "Бакалавр"
        resp_bachalor = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.bachalor_section.pk,
                                                                'section_id': self.discipline_bachalor_section.pk,
                                                                'item_id':self.theme_for_discipline_bachalor_section.pk,
                                                                'post_item': self.first_post.pk,}))

        resp_master = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.master_section.pk,
                                                                       'section_id': self.discipline_master_section.pk,
                                                                       'item_id': self.theme_for_discipline_master_section.pk,
                                                                       'post_item': self.second_post.pk, }))

        self.assertEqual(resp_bachalor.status_code, 200) # Есть права доступа к приватной ветке "Бакалаврам"
        self.assertEqual(resp_master.status_code, 403)  # Нет прав доступа к приватной ветке "Магистрам"

    def test_access_to_post_master_user(self): # пользователь с правами "Бакалавр"

        self.client.login(username='testuser2', password='1234587') # Регистрируем пользователя с правами "Магистр"
        resp_bachalor = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.bachalor_section.pk,
                                                                    'section_id': self.discipline_bachalor_section.pk,
                                                                    'item_id':self.theme_for_discipline_bachalor_section.pk,
                                                                    'post_item': self.first_post.pk,}))
        resp_master = self.client.get(reverse('post_detail', kwargs={'supersection_id': self.master_section.pk,
                                                                       'section_id': self.discipline_master_section.pk,
                                                                       'item_id': self.theme_for_discipline_master_section.pk,
                                                                       'post_item': self.second_post.pk, }))

        self.assertEqual(resp_bachalor.status_code, 200) # Есть права доступа к приватной ветке "Бакалаврам"
        self.assertEqual(resp_master.status_code, 200)  # Есть права доступа к приватной ветке "Магистрам"















