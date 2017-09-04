from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^back$', views.start),
    url(r'^submit$', views.submit),
    url(r'^succes$', views.succes),
    url(r'^delete/(?P<id>\d+$)', views.delete),
]