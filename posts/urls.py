from django.conf.urls import url, include
from .views import get_posts, post_detail, create_or_edit_post
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
]
