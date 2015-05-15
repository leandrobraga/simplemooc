from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'simplemooc.forum.views',
    url(r'^$', 'index', name='index'),
)
