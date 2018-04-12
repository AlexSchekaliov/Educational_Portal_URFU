from django.contrib import admin
from educportal.models import User
from educportal.models import AcademicGroup
from educportal.models import StudentGroupAccess

admin.site.register(User)
admin.site.register(AcademicGroup)
admin.site.register(StudentGroupAccess)


# Register your models here.
