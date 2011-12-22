from django.conf.urls.defaults import *

urlpatterns = patterns('luna.ventrilo.views',
    (r'^$', 'index'),
    (r'^(?P<server_id>\d+)/$', 'status'),
)