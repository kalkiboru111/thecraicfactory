from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    #one to one relationship between user's profile and user model and on delete of profile. Cascade deletes profile if user deleted, but not vice versa. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # set default profile photo and specifies directory where images will be uplaoded to.
    bio = models.TextField(max_length=280, default='yet another craic addict')
    profile_image = models.ImageField(upload_to='profile_pics', default='denzel.jpeg') # where profile image is stored
    
    def __str__(self):
        return f'{self.user.username} Profile'