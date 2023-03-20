from django.urls import path 
from . import views 


urlpatterns = [
    
    path('', views.getRoutes, name="routes"), 
    path('foods/', views.getFoods, name="get-food"), 
    path('add-food/', views.addFood, name="add-food"), 
    path('food/<str:pk>/', views.foodDetails), 
    
    
    
    
]