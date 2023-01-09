from django.db import models
from django.contrib.auth.models import User
import uuid  
from . import signals
from django.db.models.signals import post_save, post_delete



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage =  models.ImageField(null=True, blank=True, upload_to='profile_imgs')
    email = models.EmailField(max_length=200, blank=True, null=True)
    username  = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=False)
    
    
    def __str__(self):
        return self.username
    
    
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.firstname,
            email=user.email,
            name=f'{user.first_name} " " {user.last_name}'
        )


def deleteProfile(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteProfile, sender=Profile)

        
        

    
