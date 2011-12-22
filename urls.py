from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
#from production.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/$', 'production.views.ProductionView', name='products'),
    url(r'^', include('cms.urls')),

    (r'^tinymce/',include('tinymce.urls')),

)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns