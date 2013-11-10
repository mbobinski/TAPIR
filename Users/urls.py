from django.conf.urls import patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Users.views',
    (r'^registration/$', 'register'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
    (r'^user_panel/(?P<userid>\d+)/$', 'user_panel'),
    (r'^new_user_add/(?P<userid>\d+)/$', 'new_user_add'),
    (r'^new_user_out/(?P<userid>\d+)/$', 'new_user_out'),
    (r'^new_user/$', 'new_user'),
    (r'^about/$', 'about'),
)
