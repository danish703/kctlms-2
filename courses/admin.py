from django.contrib import admin
from .models import Course,Content,Comment
# Register your models here.
admin.site.register([Course,Content,Comment])