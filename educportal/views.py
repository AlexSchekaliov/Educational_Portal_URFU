from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from educportal.forms import SignUpForm
from educportal.models import VideoPost
from educportal.models import Discipline


# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url = reverse_lazy('login_page')


class BachalorSectionView(ListView):
    template_name = "educportal/bachelor_page.html"
    def get_queryset(self):

        return Discipline.objects.filter(for_super_section__degree="Бакалавр")


class MasterSectionView(ListView):
    template_name = 'educportal/master_page.html'
    def get_queryset(self):

        return Discipline.objects.filter(for_super_section__degree="Магистр")

class AspirantSectionView(ListView):
    template_name = 'educportal/aspirant_page.html'
    def get_queryset(self):
        return Discipline.objects.filter(for_super_section__degree="Аспирант")



class VideoListView(ListView):
    template_name = 'educportal/videolist.html'

    def get_queryset(self):
        return VideoPost.objects.filter(theme__pk=self.kwargs['pk'])
