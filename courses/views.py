from django.shortcuts import render,redirect
from .forms import CourseForm
from django.contrib import messages

# Create your views here.
def create_course(reqeust):
    form = CourseForm(reqeust.POST or None,reqeust.FILES or None)
    if reqeust.method=='POST':
        if form.is_valid():
            form.save()
            messages.add_message(reqeust,messages.SUCCESS,"Saved Successfully")
        return redirect('create_course')
    else:
        context = {
            'form':form ,
            'x':10
        }
        return render(reqeust,'create_course.html',context)