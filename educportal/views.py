from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from educportal.forms import SignUpForm

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url =  reverse_lazy('login_page')
	

