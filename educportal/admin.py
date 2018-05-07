from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from educportal.models import User
from educportal.models import AcademicGroup
from educportal.models import StudentGroupAccess
from  educportal.models import Post
from educportal.models import Theme
from educportal.models import Section
from educportal.models import SuperSection

admin.site.register(User)
admin.site.register(AcademicGroup)
admin.site.register(StudentGroupAccess)
admin.site.register(Post,SummernoteModelAdmin)
admin.site.register(Theme)
admin.site.register(Section)
admin.site.register(SuperSection)



# Register your models here.
