from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', 'detail', name='detail'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'enrollment', name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', 'undo_enrollment', name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', 'announcements', name='announcements'),

)
