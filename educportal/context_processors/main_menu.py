from django.template.context_processors import request
from educportal.models import SuperSection


def menu(request):
    super_section_list = SuperSection.objects.all()

    return {"super_section_list": super_section_list}