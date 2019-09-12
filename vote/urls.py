from django.conf.urls import url
from .views import vote

urlpatterns = [
    url(r'^vote/(?P<pk>\d+)',vote, name='vote'),
]