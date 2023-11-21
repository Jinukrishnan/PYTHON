from django.shortcuts import render
from .models  import Place
#  Create your views here.
def home(req):
    obj=Place.objects.all()
    return render(req,'index.html',{'result':obj})