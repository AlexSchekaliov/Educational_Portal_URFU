from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView, ListView, DetailView, UpdateView

from educportal.forms import SignUpForm
from educportal.models import User, Section, Post, Theme, Test



# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "educportal/register.html"
    success_url = reverse_lazy('login_page')


class SectionListView(TemplateView):
    template_name = 'educportal/section_list.html'

    def sections(self, is_guest = None):
        return Section.objects.filter(super_section__pk=self.kwargs['pk'], is_guest=is_guest)

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['section_guest'] = self.sections(is_guest=True)
        context['section'] = self.sections(is_guest=False)
        return context


class ThemeListView(ListView):
    template_name = "educportal/themes_list.html"
    context_object_name = "themes_list"

    def sections(self, is_guest=None):
        # return  Section.objects.filter(super_section__pk=self.kwargs['supersection_id'], is_guest=is_guest)
        return Section.objects.filter(super_section__section__pk=self.kwargs['section_id'], is_guest=is_guest)

    def get_context_data(self, **kwargs):
        context = super(ThemeListView, self).get_context_data(**kwargs)
        context['section_guest'] = self.sections(is_guest=True)
        context['section'] = self.sections(is_guest=False)
        return context

    def get_queryset(self):
        return Theme.objects.filter(discipline__pk=self.kwargs['section_id']).order_by('created_date')


class PostTestListView(ListView):
    template_name = 'educportal/post_test_list.html'
    context_object_name = 'post_list'

    def get_test(self):
        return Test.objects.filter(theme__pk=self.kwargs['item_id']).order_by('created_date')

    def get_context_data(self, **kwargs):
        context = super(PostTestListView,self).get_context_data(**kwargs)
        context['test_list'] = self.get_test()
        return context

    def get_queryset(self):
        return Post.objects.filter(theme__pk=self.kwargs['item_id']).order_by('created_date')

class PostDetailView(DetailView):
    template_name = 'educportal/post_detail.html'
    model = Post
    pk_url_kwarg = "post_item"
    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        context ['post_list'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Post.objects.filter(theme__pk=self.kwargs['item_id']).order_by('created_date')


# class TaskListView ()

class ChangeUserInfoView(UpdateView):
    model = User
    fields = ['username','email', 'phone_number']
    template_name = 'educportal/change_personal_info.html'
    success_url = reverse_lazy('personal_info')

    def get_object(self, queryset=None):
        return self.request.user
