from django.urls import path
from . import views
from new import settings
from django.conf.urls.static import static

app_name='api'

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<str:id>/',views.details,name='details'),
    path('cart/<str:id>/',views.cart,name='cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    