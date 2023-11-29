from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse
# Create your views here.
def home(req):
    movies=Movie.objects.all()
    return render(req,'index.html',{'movies':movies})


def detail(req,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(req,'MovieDetail.html',{"movie":movie})