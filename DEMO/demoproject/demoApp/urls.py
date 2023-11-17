
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.demo,name='demo'),
    path('contact/',views.contact,name='contact')
]
