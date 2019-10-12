from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    #one to one relationship between user's profile and user model and on delete of profile. Cascade deletes profile if user deleted, but not vice versa. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # set default profile photo and specifies directory where images will be uplaoded to.
    profile_image = models.ImageField(upload_to='profile_pics', blank=True, default='denzel.jpeg') # where is stored the user profile image
    
    def __str__(self):
        return f'{self.user.username} Profile'
   
            
    
    
