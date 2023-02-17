from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from courses.models import Course
from .models import Enrollment
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def enroll_course(request, id):
    if request.user.is_staff == 0:
        try:
            e = Enrollment(course_id=id,user_id=request.user.id)
            e.save()
            messages.add_message(request,messages.SUCCESS,"Enroll Successfully")
        except:
            messages.add_message(request,messages.ERROR,"Already Enrolled")
        finally:
            return redirect('course_info', id)
    else:
        messages.add_message(request, messages.ERROR, "please ! login from student account")
        return redirect('signin')