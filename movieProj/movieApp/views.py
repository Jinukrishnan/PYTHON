from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Movie
from .forms import MovieForm



def index(request):
    content=Movie.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = int(request.POST.get('year'))
        img = request.FILES['image']
        print(img)
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    #DJANGO FORM METHOD
    # movie=Movie.objects.get(id=id)
    # form=MovieForm(request.POST or None,request.FILES,instance=movie)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # return render(request,'edit.html',{'form':form,'movie':movie})
    # NORMAL FORM UPDATION METHOD

    movie = get_object_or_404(Movie, id=id)
    if request.method=='POST':
            name=request.POST.get('name')
            desc=request.POST.get('desc')
            year=request.POST.get('year')
            img=request.FILES['image']
            imgname=str(img)
            movie.img.save(imgname, img, save=True)
            Movie.objects.filter(id=id).update(name=name,desc=desc,year=year)
            return  redirect('/')


    return render(request,'edit.html',{'movie':movie})


def delete(request,id):
    if request.method=='POST':
        deldata=Movie.objects.get(id=id)

        deldata.delete()
        return redirect('/')
    return render(request,'delete.html')







# USER AUTHENTICATION PART
def register(request):
    if request.method=='POST':
        if request.method=='POST':
            username=request.POST.get('user_name')
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email= request.POST.get('email')
            pwd = request.POST.get('pwd')
            cnfpwd = request.POST.get('cnfpwd')
            if pwd==cnfpwd:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username Already Exist")
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Exist")
                    return redirect('/register')
                else:
                    user=User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd)
                    user.save()
                return redirect('/')
            else:
                messages.info(request, "Password Not Match")
                return redirect('/register')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Entry')
            return redirect('/login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')