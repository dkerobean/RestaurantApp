from django.contrib import admin
from .models import Food, FoodType, Category

# Register your models here.

admin.site.register(Food), 
admin.site.register(FoodType), 
admin.site.register(Category)
