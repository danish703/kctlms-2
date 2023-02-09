from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateField(auto_now=True)
    hours = models.PositiveIntegerField(default = 2)
    course_image = models.ImageField(upload_to='course/')

    def __str__(self):
        return self.course_name


class Content(models.Model):
    content_title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.content_title

class Comment(models.Model):
    comment_msg = models.TextField()
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    commented_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment_msg

