from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'userpathnodes', views.UserPathNodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^userpath/(?P<path_id>.*)/$', views.get_userpath, name='userpath'),
    url(r'^userpathnode/(?P<user_id>.*)/(?P<node_id>.*)/', 
        views.userpathnode, name='userpathnode'),
]
