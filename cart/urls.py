from django.urls import path
from . import views
app_name='cart'
urlpatterns = [

    path('add_cart/<int:pid>/',views.addCart,name='add_cart'),
    path('cart_details/',views.cartDetails,name='cart_details'),
    
]
