
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from restaurant import views


router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api/',include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
]
