from django.conf.urls import url, include
from .views import get_posts, post_detail, create_or_edit_post, vote_up, vote_count, vote_down

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/vote_up/$', vote_up, name='vote_up'),
    url(r'^(?P<pk>\d+)/vote_down/$', vote_down, name='vote_down'),
    url(r'^(?P<pk>\d+)/vote_up/$', vote_count, name='vote_count'),
    
]
