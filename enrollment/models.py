from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.
class Enrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    enroll_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course