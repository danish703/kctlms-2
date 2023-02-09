from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def home(request):
    return render(request,'index.html')

def signin(request):
    if request.method=='POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(username=email,password=password1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
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

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')