from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from educportal.models import User, AcademicGroup,GroupAccess,Post,Theme,Section,SuperSection,Test,Task,TaskAnswer

admin.site.register(User)
admin.site.register(AcademicGroup)
admin.site.register(GroupAccess)
admin.site.register(SuperSection)
admin.site.register(Post,SummernoteModelAdmin)
admin.site.register(Theme)
admin.site.register(Section)
admin.site.register(Test)
admin.site.register(Task,SummernoteModelAdmin)
admin.site.register(TaskAnswer, SummernoteModelAdmin)


# Register your models here.
