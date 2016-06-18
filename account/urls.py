from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'', include('registration.urls')),
    (r'^(?P<username>\w+)/$', 'account.views.profile'),
)