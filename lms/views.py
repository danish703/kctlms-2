from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from courses.models import Course

def home(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request,'index.html',context)

def signin(request):
    if request.method=='POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(username=email,password=password1)
        if user is not None:
            login(request,user)
            return redirect('staff_dashboard')
        else:
            messages.add_message(request,messages.ERROR,"username and password does not match")
            return redirect('signin')
    else:
        return render(request,'signin.html')



def signup(request):
    if request.method=='POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            user = User(first_name=firstname,last_name=lastname,username=email)
            user.set_password(password1)
            user.save()
            messages.add_message(request,messages.SUCCESS,"User account created")
            return redirect('signin')
        else:
            messages.add_message(request,messages.ERROR,"Password and Password Confirmation does not match")
            return redirect('signup')
    else:
        return render(request,'signup.html')

def student_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')

def staff_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff==1:
            return render(request,'superdashboard.html')
        else:
            return redirect('student_dashboard')
    else:
        return redirect('signin')


def signout(reqeust):
    logout(reqeust)
    return redirect('signin')