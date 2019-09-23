from django.conf.urls import url, include
from .views import upvote

urlpatterns = [
    url(r'^upvote/', upvote, name='upvote')
    ]

