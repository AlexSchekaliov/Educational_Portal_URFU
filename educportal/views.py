from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from educportal.forms import SignUpForm

# Create your views here.
from educportal.models import VideoPost


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url =  reverse_lazy('login_page')

class VideoListView (ListView):


    def get_queryset(self):

        return VideoPost.objects.filter(theme__pk=self.kwagrs['pk'])
	

