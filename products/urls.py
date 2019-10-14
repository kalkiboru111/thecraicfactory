from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
   url(r'^all_products/(?P<id>\d+)$', all_products, name='all_products'),
]