from django.contrib import admin
from educportal.models import User
from educportal.models import AcademicGroup
from educportal.models import StudentGroupAccess
from  educportal.models import VideoPost
from educportal.models import Theme
from educportal.models import Section

admin.site.register(User)
admin.site.register(AcademicGroup)
admin.site.register(StudentGroupAccess)
admin.site.register(VideoPost)
admin.site.register(Theme)
admin.site.register(Section)



# Register your models here.
