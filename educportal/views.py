from django.urls import reverse_lazy
# from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from educportal.forms import SignUpForm
from educportal.models import VideoPost
from educportal.models import Section


# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url = reverse_lazy('login_page')


class SectionListView(TemplateView):
        template_name = 'educportal/template_section.html'

        def sections(self, is_guest = None, **kwargs):
            return Section.objects.filter(for_super_section__degree=self.kwargs['degree'], is_guest=is_guest)

        def get_context_data(self, **kwargs):
            context = super(SectionListView, self).get_context_data(**kwargs)
            context['section_guest'] = self.sections(is_guest=True)
            context['section'] = self.sections(is_guest=False)
            context['title_page']= self.kwargs['title_page']
            return context

class VideoListView(TemplateView):
    template_name = 'educportal/videolist.html'

    def get_queryset(self):
        return VideoPost.objects.filter(theme__pk=self.kwargs['pk'])
