from django.conf.urls.defaults import *

urlpatterns = patterns('luna.forum.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^(?P<topic_id>\d+)/$', 'show'),
    (r'^(?P<topic_id>\d+)/reply/$', 'reply'),
    (r'^(?P<topic_id>\d+)/delete/$', 'delete_topic'),
    (r'^(?P<topic_id>\d+)/post/(?P<post_id>\d+)/edit/$', 'edit'),
    (r'^(?P<topic_id>\d+)/post/(?P<post_id>\d+)/delete/$', 'delete_post'),
    (r'^tag/(?P<tag_name>\w+)/$', 'with_tag'), 
    (r'^tag/(?P<tag_name>\w+)/page/(?P<page_number>\d+)/$', 'with_tag' ),
)