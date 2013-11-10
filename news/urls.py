from django.conf.urls import patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('news.views',
    (r'^$', 'index'),
    (r'^add/$', 'add_post'),
    (r'^edit/(?P<postid>\d+)/$', 'edit_post'),
)
