
from django.urls import path
from searchApp import views
app_name='searchapp'
urlpatterns = [
    path('',views.SearchResult,name='search' )
    
  
]
