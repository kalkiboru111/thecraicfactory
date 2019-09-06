from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vote.models import VoteModel


# Create your models here.

class Post(VoteModel, models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    friend_tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # total_votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# class Votes(models.Model):
#     vote_issue = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)

#     def __str__(self):
#         return self.user
