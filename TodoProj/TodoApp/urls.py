
from django.urls import path
from . import views
urlpatterns = [
  
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.Delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]
