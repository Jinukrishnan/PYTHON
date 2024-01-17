from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from .serializers import PhoneSerializers
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.
def home(req):
    
    
    return render(req,'index.html')

@csrf_exempt
def addPhone(req):
    if req.method=='POST':
        x=JSONParser().parse(req)
        print(x)
        s=PhoneSerializers(data=x)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_401_UNAUTHORIZED)
        

def getPhone(req):
    if req.method=='GET':
        phone=Student.objects.all()
        s=PhoneSerializers(phone,many=True)
        print("sasa",s)
    return JsonResponse(s.data,safe=False)


    