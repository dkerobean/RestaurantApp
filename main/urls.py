from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('reservation/', views.reservation, name="reservation"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu/<str:pk>', views.foodDetails, name="foodDetails"),


    
]
