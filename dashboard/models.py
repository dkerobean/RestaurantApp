
from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    


class FoodType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=True)
    food_type = models.ForeignKey(FoodType, null=True,
                                  blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,
                                 blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True,
         upload_to='food_img', default="default_food.png")
    price = models.IntegerField(blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    

    
    
    
    
    
    
