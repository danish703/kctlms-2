from django.shortcuts import render,redirect
from .forms import CourseForm
from django.contrib import messages
from .models import Course
# Create your views here.
def create_course(reqeust):
    form = CourseForm(reqeust.POST or None,reqeust.FILES or None)
    if reqeust.method=='POST':
        if form.is_valid():
            form.save()
            messages.add_message(reqeust,messages.SUCCESS,"Saved Successfully")
            return redirect('course_list')
    context = {
            'form':form
        }
    return render(reqeust,'create_course.html',context)

def course_list(request):
    courses = Course.objects.all() #reterive all the records form the courses table.
    context = {
        'courses':courses
    }
    return render(request,'course_list.html',context)

def course_details(request,id):
    context = {
        'course':Course.objects.get(pk=id)
    }
    return render(request,'course_details.html',context)

def course_edit(request,id):
    course = Course.objects.get(pk=id)
    form = CourseForm(request.POST or None,request.FILES or None,instance = course)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('course_details',id)
    context = {
        'form':form
    }
    return render(request,'course_edit.html',context)

def course_delete(request,id):
    course = Course.objects.get(pk=id)
    course.delete()
    messages.add_message(request,messages.SUCCESS,"successfully deleted")
    return redirect('course_list')