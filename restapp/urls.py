
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home" ),
    path('addphone/',views.addPhone,name="addPhone" ),
    path('getphone/',views.getPhone,name="getphone" ),

    
]
