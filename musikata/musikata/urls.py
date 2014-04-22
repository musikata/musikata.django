from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^path/', include('path.urls')),
    url(r'^client/', include('musikata_client.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
