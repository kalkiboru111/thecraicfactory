from django.conf.urls import url, include
from .views import upvote

urlpatterns = [
    url(r'^upvote/(?P<pk>\d+)', upvote, name='upvote')
    ]