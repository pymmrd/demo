# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include

urlpatterns = patterns(r'cans.views', 
	(r'creation/(?P<name>.+)/$', 'show_creation'),
)

