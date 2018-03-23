from django.shortcuts import render

from django.views.generic.edit import FormView
from educportal.forms import SignUpForm

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'home_page.html'
    success_url = '/'

    def form_valid(self, form):
        
        return redirect(self.get_success_url())

	def form_invalid(self, form):

		return 

# Create your views here.

def home_page(request):
	return render(request, 'educportal/home_page.html', {})
	

