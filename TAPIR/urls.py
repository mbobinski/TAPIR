from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TAPIR.views.home', name='home'),
    # url(r'^TAPIR/', include('TAPIR.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('Users.urls')),
    url(r'^teamplay/', include('teamplay.urls')),
    url(r'^rank/', include('rank.urls')),
    url(r'^', include('news.urls')),
    url(r'^mumble/$', 'TAPIR.views.mumble'),
    url(r'^programs/$', 'TAPIR.views.programs'),
    url(r'^rules/$', 'TAPIR.views.rules'),
)
