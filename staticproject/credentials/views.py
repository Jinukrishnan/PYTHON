from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
# Create your views here.
def register(req):
    if req.method=='POST':
        username=req.POST['username']
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email=req.POST['email']
        password=req.POST['password']
        c_password=req.POST['c_password']
        print(username,first_name,last_name,email,password,c_password)
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(req,"usernameTaken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                # messages.info(req,"User craeted")
                return redirect('login')
        else:
            # print('password not matched')
            messages.info(req,"password not match")
            return redirect('register')
        return redirect('/')
    return  render(req,'register.html')


def login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,'invalid credentials')
            return redirect('login')
    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    return redirect('/')