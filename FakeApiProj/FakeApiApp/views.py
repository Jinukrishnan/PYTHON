from django.shortcuts import render
import requests
# Create your views here.
def index(req):
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    print(res)
    if res.status_code==200:
        data=res.json()
        print(data)
    return render(req,'index.html',{'data':data})