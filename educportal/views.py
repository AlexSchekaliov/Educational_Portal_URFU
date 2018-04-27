from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView

from educportal.forms import SignUpForm
from educportal.models import VideoPost, SuperSection
from educportal.models import Section


# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url = reverse_lazy('login_page')



# class SuperSectionListView(ListView):
#     template_name = "educportal/home_page.html"
#
#     def get_queryset(self):
#         return SuperSection.objects.all()


class SectionListView(TemplateView):
        template_name = 'educportal/template_section.html'

        def sections(self, is_guest = None):
            return Section.objects.filter(super_section__pk=self.kwargs['pk'], is_guest=is_guest)

        def get_context_data(self, **kwargs):
            context = super(SectionListView, self).get_context_data(**kwargs)
            context['section_guest'] = self.sections(is_guest=True)
            context['section'] = self.sections(is_guest=False)
            return context

        # def get_queryset(self):
        #     return Section.objects.filter(for_super_section__pk=self.kwargs['pk'])


class VideoListView(SectionListView):
    template_name = 'educportal/videolist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        return context

    def get_queryset(self):
        return VideoPost.objects.filter(theme__pk=self.kwargs['pk'])
