from django.contrib import admin
from app1.models import CoursesStoreModel


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('id','teacher_id','course_name','dept','course_img','course_video', 'first_upload','last_upload')

admin.site.register(CoursesStoreModel, CourseModelAdmin)




