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
from django.urls import path
from django.views.generic import TemplateView

from educportal.views import SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='educportal/home_page.html'), name = 'home_page'),
    path(r'register/', SignUpView.as_view(), name = 'reg_page'),
    path(r'login/', LoginView.as_view(template_name='educportal/login.html'), name = 'login_page'),
    path(r'logout/', LogoutView.as_view(), name = 'logout'),
    path(r'profile/', TemplateView.as_view(template_name='educportal/profile_page.html'), name = 'profile_page'),
    path(r'bachelor/', TemplateView.as_view(template_name='educportal/bachelor_page.html'), name = 'bachelor_page'),
    path(r'master/', TemplateView.as_view(template_name='educportal/master_page.html'), name = 'master_page'),
    path(r'aspirant/', TemplateView.as_view(template_name='educportal/aspirant_page.html'), name = 'aspirant_page'),

]