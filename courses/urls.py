from django.urls import path
from .views import (create_course,course_list,course_details,
                    course_edit,course_delete,create_content,content_list,
                    content_edit,delete_content,course_info)
urlpatterns = [
  path('create-course/',create_course,name='create_course'),
  path('list/',course_list,name='course_list'),
  path('details/<int:id>',course_details,name='course_details'),
  path('edit/<int:id>',course_edit,name='course_edit'),
  path('delete/<int:id>',course_delete,name='course_delete'),
  path('create-content/<int:id>',create_content,name='create_content'),
  path('view-content/<int:id>',content_list,name='content_list'),
  path('edit-content/<int:id>',content_edit,name='content_edit'),
  path('delete-content/<int:id>',delete_content,name='delete_content'),
  path('course-info/<int:id>',course_info,name='course_info'),

]