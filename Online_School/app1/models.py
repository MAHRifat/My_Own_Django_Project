from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.

class CoursesStoreModel(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30)
    dept = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_img = models.ImageField(upload_to='img/courses', default=False)
    course_video = models.FileField(upload_to='files/courses',default=False)
    course_description = models.CharField(max_length=200)
    first_upload = models.DateTimeField(auto_now_add=True)
    last_upload = models.DateTimeField(auto_now=True) 
    def __str__(self) -> str:
        return f"{self.id}"
    

