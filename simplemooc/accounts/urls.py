from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^entrar/', 'django.contrib.auth.views.login', name='index'),
)
