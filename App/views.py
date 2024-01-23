from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    url='https://dummyjson.com/products'
    response=requests.get(url)
    data=response.json()
    
    return render(request,'index.html',{'data':data})

def details(request,id):
    url='https://dummyjson.com/products/'+id
    response=requests.get(url)
    data=response.json()
    return render(request,'details.html',{'data':data})

def cart(request,id):
    url='https://dummyjson.com/products/'+id
    response=requests.get(url)
    data=response.json()
    return render(request,'cart.html',{'data':data})

