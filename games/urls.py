from django.conf.urls.defaults import *

urlpatterns = patterns('games.views',
    (r'^$', 'index'),
    (r'^tag/(?P<tag_name>\w+)/$', 'with_tag'), 
    (r'^tag/(?P<tag_name>\w+)/page/(?P<page_number>\d+)/$', 'with_tag' ),
)