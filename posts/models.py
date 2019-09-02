from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=1)
    tag = models.CharField(max_length=30, blank=True, null=True)
    friend_tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title