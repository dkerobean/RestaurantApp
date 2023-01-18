from django.db import models
import uuid
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True,
                                      upload_to='profile_img', default='profiles/user-default.png')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
    
    
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
