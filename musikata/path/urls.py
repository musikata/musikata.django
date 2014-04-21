from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userpathnode', views.get_userpathnode, name='userpathnode')
]
