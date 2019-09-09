from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
	
class Vote(models.Model):
	vote_name = models.fields.CharField(max_length=128)

class UserVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

# Model for Posts here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    friend_tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title




