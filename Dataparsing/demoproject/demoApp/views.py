from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    name="Synnefo"
    return render(request,'index.html',{'obj':name})

def add(request):
    x=int(request.GET['fno'])
    y=int(request.GET['sno'])
    z=x+y
    return render(request,'result.html',{'result':z})