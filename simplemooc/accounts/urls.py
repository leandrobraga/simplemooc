from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^entrar/', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='index'),
    url(r'^registre-se/', 'simplemooc.accounts.views.register', name='register'),
)
