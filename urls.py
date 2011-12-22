from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'luna.home.views.index'),
    (r'^dingus/$', 'luna.home.views.dingus'),
    (r'^forum/', include('luna.forum.urls')),
    (r'^games/', include('luna.games.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^account/', include('luna.account.urls')),
    (r'^accounts/', 'luna.account.views.index'),
    (r'^ventrilo/', include('luna.ventrilo.urls')),
)

from luna.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
if DEBUG:
    from django.views.static import serve

    url = MEDIA_URL
    if url.startswith('/'): url = url[1:]

    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % url, serve, {'document_root': MEDIA_ROOT}),
        (r'^404/', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        (r'^500/', 'django.views.generic.simple.direct_to_template', {'template': '500.html'})
    )

    del(url, serve)