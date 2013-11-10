from django.conf.urls import patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('rank.views',
    (r'^$', 'show_ranking'),
    (r'^update/$', 'ranking_update'),
    (r'^update/live/$', 'ranking_live_update'),
)
