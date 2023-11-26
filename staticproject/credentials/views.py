from django.contrib.auth.models import User
from django.shortcuts import render

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
            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
            print('user created')
        else:
            print('password not matched')

    return  render(req,'register.html')