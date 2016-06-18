from django.conf.urls import patterns, include
from django.contrib import admin
from settings import DEBUG, MEDIA_URL, MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'home.views.index'),
                       (r'^dingus/$', 'home.views.dingus'),
                       (r'^forum/', include('forum.urls')),
                       (r'^games/', include('games.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^account/', include('account.urls')),
                       (r'^accounts/', 'account.views.index'),
                       (r'^ventrilo/', include('ventrilo.urls'))
                       )

if DEBUG:
    from django.views.static import serve

    url = MEDIA_URL
    if url.startswith('/'):
        url = url[1:]

    urlpatterns += patterns('',
                            (r'^%s(?P<path>.*)$' % url, serve, {'document_root': MEDIA_ROOT}),
                            (r'^404/', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
                            (r'^500/', 'django.views.generic.simple.direct_to_template', {'template': '500.html'})
                            )

    del (url, serve)
