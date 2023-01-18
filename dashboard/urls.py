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
    
    path('messages/', views.contact, name="messages"),
    path('message/delete/<str:pk>/', views.deleteContact, name="deleteMessage"),
    path('reservations/', views.reservation, name="reservations"),
    path('reservation/delete/<str:pk>/', views.deleteReservation, name="deleteReservation"),
    path('category/create/', views.createCategory, name="categories"),
    path('category/delete/<str:pk>/', views.deleteCategory, name="deleteCategory"),
    path('foodtype/create/', views.createFoodtype, name="foodtype"),
    path('foodtype/delete/<str:pk>/', views.deleteFoodtype, name="deleteFoodtype"),
    path('profile/<str:pk>/', views.viewProfile, name="profile"),
    path('create/user/', views.createUser, name="createUser"),
    path('users/', views.viewUsers, name="viewUsers"),
    path('users/delete/<str:pk>/', views.deleteUsers, name="deleteUser"),

    
    path('permission-error/', views.permissionEror, name="permission"),








    
    
    
    
]


