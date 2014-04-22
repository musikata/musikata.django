from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'userpathnodes', views.UserPathNodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^userpathnode/', views.get_userpathnode, name='userpathnode'),
]
