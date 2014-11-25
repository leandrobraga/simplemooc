from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'detail', name='detail'),
)
