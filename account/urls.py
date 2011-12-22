from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'', include('registration.urls')),
    (r'^(?P<username>\w+)/$', 'luna.account.views.profile'),
)