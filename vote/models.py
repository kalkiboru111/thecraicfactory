from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')