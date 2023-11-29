
from django.urls import path
from . import views
app_name='movieApp'
urlpatterns = [
   
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.detail,name='detail')
]
