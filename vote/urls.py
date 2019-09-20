from django.conf.urls import url, include
from vote import urls as urls_upvote

urlpatterns = [
    url(r'^upvote/', include(urls_upvote)
    ]

