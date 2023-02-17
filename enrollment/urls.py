from django.urls import path
from .views import enroll_course
urlpatterns = [
 path('enroll-course/<int:id>',enroll_course,name="enroll_course"),
]