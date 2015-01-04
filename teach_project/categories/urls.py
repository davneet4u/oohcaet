from __future__ import absolute_import
from django.conf.urls import patterns,url
from .views import index

urlpatterns = patterns('',
                       	  url(r'^$',index, name='index'))


