from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)
    # The rest of code...

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # The rest of code...

class Voter(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
