from django.urls import path
from .views import create_course,course_list,course_details,course_edit,course_delete
urlpatterns = [
  path('create-course/',create_course,name='create_course'),
  path('list/',course_list,name='course_list'),
  path('details/<int:id>',course_details,name='course_details'),
  path('edit/<int:id>',course_edit,name='course_edit'),
  path('delete/<int:id>',course_delete,name='course_delete')
]