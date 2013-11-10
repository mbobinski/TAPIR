from django.conf.urls import patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('teamplay.views',
    (r'^$', 'teamplay'),
    (r'^(?P<userid>\d+)/$', 'sign'),
    (r'^out/(?P<userid>\d+)/$', 'sign_out'),
    (r'^details/(?P<userid>\d+)/$', 'details'),
    (r'^add/$', 'add_teamplay'),
    (r'^edit/(?P<teamid>\d+)/$', 'edit_teamplay'),

)
