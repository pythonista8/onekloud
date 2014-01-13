from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.pages.views',
    url(r'^$', 'home', name='home'),
    url(r'^pricing/$', 'pricing', name='pricing'),
    url(r'^contact/$', 'contact', name='contact'),

    url(r'^privacy/$', 'privacy', name='privacy'),
    url(r'^terms-of-service/$', 'terms_of_service', name='terms_of_service'),
)
