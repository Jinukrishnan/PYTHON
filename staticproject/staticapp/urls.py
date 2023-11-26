
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('dest/',views.dest,name='dest'),
    path('news/',views.news,name='news'),
    path('elements/',views.elements,name='elements'),

]