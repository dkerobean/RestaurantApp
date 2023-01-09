from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.userLogin, name='login'), 
    path('logout/', views.userLogout, name="logout"),
    path('home/', views.dashbord, name="dashboard"), 
    
    path('addMenu/', views.createFood, name="addMenu"), 
    path('delete/<str:pk>/', views.deleteFood, name="deleteFood"),
    path('view/<str:pk>/', views.foodDetail, name="foodDetail"),
    path('update/<str:pk>/', views.updateFood, name="updateFood"),
    path('viewMenu/', views.viewMenu, name="viewMenu"),
    
    
]


