
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.demo,name='demo'),
    path('add/',views.add,name='add')
]
