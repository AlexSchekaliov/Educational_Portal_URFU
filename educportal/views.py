from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from educportal.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url =  reverse_lazy('auth_page')






'''
class SignInView(FormView):
    form_class = AuthenticationForm
    template_name = "educportal/login.html"
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):

        login(self.request, form.get_user())

        return redirect(self.get_success_url())
'''
class HomePageView(TemplateView):

    template_name = "educportal/home_page.html"
	

