from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def index(req):
    obj=place.objects.all
    obj2=team.objects.all
    return render(req,'index.html',{"result":obj,"team":obj2})
def contact(req):
    return render(req,'contact.html')
def dest(req):
    return render(req,'destinations.index')
def news(req):
    return render(req,'news.html')
def elements(req):
    return render(req,'elements.html')