from django.db import models
import uuid 


class Reservation(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    date_time = models.DateTimeField()
    no_of_people = models.IntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name
