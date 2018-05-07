"""urfuwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView

from educportal.views import SignUpView, SectionListView, ThemeListView, PostListView, PostDetailView, ChangeUserInfoView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,PasswordChangeDoneView




urlpatterns = [
    path(r'', TemplateView.as_view(template_name="educportal/home_page.html"), name = 'home_page'),
    path(r'register/', SignUpView.as_view(), name = 'reg_page'),
    path(r'login/',    LoginView.as_view(template_name='educportal/login.html'), name = 'login_page'),
    path(r'logout/',   LogoutView.as_view(), name = 'logout'),
    path(r'profile/',  TemplateView.as_view(template_name='educportal/profile_page.html'), name = 'profile_page'),
    path(r'profile/personal_info',  TemplateView.as_view(template_name='educportal/personal_info.html'), name = 'personal_info'),
    path(r'profile/change_personal_info', ChangeUserInfoView.as_view(), name = 'change_personal_info'),
    path(r'profile/change_personal_info/password_change/', PasswordChangeView.as_view(template_name='educportal/change_user_password.html', success_url=reverse_lazy('change_user_password_done')), name = 'change_user_password'),
    path(r'profile/change_personal_info/password_change/done', PasswordChangeDoneView.as_view(template_name='educportal/personal_info.html'), name = 'change_user_password_done'),
    path(r'degrees/<int:pk>/', SectionListView.as_view(), name='bachelor_page'),
    path(r'<int:section_id>/themes', ThemeListView.as_view(),name = 'theme_list'),
    path(r'<int:section_id>/themes/<int:item_id>/posts', PostListView.as_view(),name = 'post_list'),
    path(r'<int:section_id>/themes/<int:item_id>/post/<int:post_item>', PostDetailView.as_view(), name = 'post_detail'),
]