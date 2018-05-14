from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from educportal.models import User, AcademicGroup,StudentGroupAccess,Post,Theme,Section,SuperSection,Test,Task,TaskAnswer,\
    Department,Student,Teacher


admin.site.register(User)
admin.site.register(AcademicGroup)
admin.site.register(StudentGroupAccess)
admin.site.register(Post,SummernoteModelAdmin)
admin.site.register(Theme)
admin.site.register(Section)
admin.site.register(SuperSection)
admin.site.register(Test)
admin.site.register(Task)
admin.site.register(TaskAnswer)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Teacher)



# Register your models here.
