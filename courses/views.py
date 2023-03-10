from django.shortcuts import render,redirect,get_object_or_404
from .forms import CourseForm,ContentForm
from django.contrib import messages
from .models import Course,Content
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def course_list(request):
    courses = Course.objects.all() #reterive all the records form the courses table.
    context = {
        'courses':courses
    }
    return render(request,'course_list.html',context)

@login_required(login_url='signin')
def course_details(request,id):
    context = {
        'course':Course.objects.get(pk=id)
    }
    return render(request,'course_details.html',context)

@login_required(login_url='signin')
def course_edit(request,id):
    #course = Course.objects.get(pk=id)
    course = get_object_or_404(Course,pk=id)
    form = CourseForm(request.POST or None,request.FILES or None,instance = course)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('course_details',id)
    context = {
        'form':form
    }
    return render(request,'course_edit.html',context)

@login_required(login_url='signin')
def course_delete(request,id):
    #course = Course.objects.get(pk=id)
    course = get_object_or_404(Course,pk=id)
    course.delete()
    messages.add_message(request,messages.SUCCESS,"successfully deleted")
    return redirect('course_list')

@login_required(login_url='signin')
def create_content(request,id):
    form = ContentForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.course_id = id
        data.save()
        messages.add_message(request,messages.SUCCESS,"Content created successfully")
        return redirect('content_list',id)
    context = {
            'form':form
        }
    return render(request,'create_content.html',context)


@login_required(login_url='signin')
def content_list(request,id):
    content = Content.objects.filter(course_id=id)
    context = {
        'contents':content
    }
    return render(request,'view_content.html',context)


@login_required(login_url='signin')
def content_edit(request,id):
    #content = Content.objects.get(pk=id)
    content = get_object_or_404(Content,pk=id)
    form = ContentForm(request.POST or None,instance=content)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Updated successfully")
        return redirect('content_list',content.course_id)
    context = {
        'form':form
    }
    return render(request,'content_edit.html',context)

@login_required(login_url='signin')
def delete_content(request,id):
    #content = Content.objects.get(pk=id)
    content = get_object_or_404(Content,pk=id)
    course_id = content.course_id
    content.delete()
    messages.add_message(request,messages.SUCCESS,"Deleted Successfully")
    return redirect('content_list',course_id)

def course_info(request,id):
    course = get_object_or_404(Course,id=id)
    context = {
        'course':course
    }
    return render(request,'course_info.html',context)

