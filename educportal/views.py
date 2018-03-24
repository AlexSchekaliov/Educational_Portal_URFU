from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.views.generic.edit import FormView
from educportal.forms import SignUpForm

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'home_page.html'
    success_url =  reverse_lazy('home_page')

    def form_valid(self, form):
        
        return redirect(self.get_success_url())

	def form_invalid(self, form):

		return 

# Create your views here.


class HomePageView(TemplateView):

    template_name = "educportal/home_page.html"
	

