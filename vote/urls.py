from django.conf.urls import url
from .views import upvote

urlpatterns = [
    url(r'^upvote/(?P<pk>\d+)', upvote, name='upvote'),
]