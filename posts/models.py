from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    votes_total = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    friend_tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_created')
    craic_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
