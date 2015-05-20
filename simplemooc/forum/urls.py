from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'simplemooc.forum.views',
    url(r'^$', 'index', name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', 'index', name='index_tagged'),
    url(r'^(?P<slug>[\w_-]+)/$', 'thread', name='thread'),
    url(r'^respostas/(?P<pk>\d+)/correta/$', 'reply_correct', name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta/$', 'reply_correct', name='reply_incorrect'),

)
