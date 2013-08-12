from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	(r'^$', direct_to_template, {'template': 'shipin1.html'}, 'home'),
	(r'^shipin/$', direct_to_template, {'template': 'shipin1.html'}, 'shipin'),
	(r'^pibao/$', direct_to_template, {'template': 'content.html'}, 'pibao'),
	(r'^shenghuo/$', direct_to_template, {'template': 'content.html'}, 'shenghuo'),
	(r'^diy/$', direct_to_template, {'template': 'content.html'}, 'diy'),
	(r'^yishu/$', direct_to_template, {'template': 'content.html'}, 'yishu'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	(r'^', include('cans.urls')),

)
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
    )   


