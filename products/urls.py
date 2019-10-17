from django.conf.urls import url, include
from .views import all_products
from posts.models import Post

urlpatterns = [
   url('^(?P<pk>\d+)$', all_products, name='all_products'),
]