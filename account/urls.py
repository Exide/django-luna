from django.conf.urls import patterns, include

urlpatterns = patterns('',
                       (r'', include('registration.urls')),
                       (r'^(?P<username>\w+)/$', 'account.views.profile'),
                       )
